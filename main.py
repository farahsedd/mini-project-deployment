import random
import string
from prometheus_client import start_http_server, Counter, Summary, Gauge
import time

# Metrics
passwords_generated = Counter('passwords_generated', 'Number of passwords generated')
generation_duration = Summary('password_generation_duration_seconds', 'Time taken to generate a password')
password_length_gauge = Gauge('password_length', 'Length of the generated password')

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generates a secure password based on the given parameters."""
    if length < 4:
        raise ValueError("The length must be at least 4 to include different types of characters.")
    
    # Set the password length gauge
    password_length_gauge.set(length)
    print(f"DEBUG: Set password_length_gauge to {length}")
    
    # Define the character pool based on user choices
    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    # Measure password generation duration
    start_time = time.time()
    password = ''.join(random.choices(char_pool, k=length))
    duration = time.time() - start_time
    generation_duration.observe(duration)  # Record the duration
    print(f"DEBUG: Observed generation_duration {duration}")
    
    # Increment the counter for passwords generated
    passwords_generated.inc()
    print(f"DEBUG: Incremented passwords_generated counter")

    return password

if __name__ == "__main__":

    # Start the Prometheus HTTP server to expose the metrics
    start_http_server(8000)  # Expose metrics on port 8000
    
    password = generate_password(12, 'y', 'n', 'n')
    password = generate_password(8, 'n', 'n', 'n')
    password = generate_password(15, 'y', 'y', 'y')
    password = generate_password(8, 'y', 'n', 'n')
    password = generate_password(8, 'n', 'y', 'y')
    print("Welcome to the secure password generator!")
    length = int(input("Enter the length of the password (min 4): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    

    try:
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
