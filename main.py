import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """Génère un mot de passe sécurisé basé sur les paramètres donnés."""
    if length < 4:
        raise ValueError("La longueur doit être au moins 4 pour inclure différents types de caractères.")

    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password = ''.join(random.choices(char_pool, k=length))
    return password

if __name__ == "__main__":
    print("Bienvenue dans le générateur de mot de passe sécurisé!")
    length = int(input("Entrez la longueur du mot de passe (min 4): "))
    use_uppercase = input("Inclure des lettres majuscules? (y/n): ").lower() == 'y'
    use_digits = input("Inclure des chiffres? (y/n): ").lower() == 'y'
    use_symbols = input("Inclure des symboles? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print(f"Mot de passe généré : {password}")
    except ValueError as e:
        print(f"Erreur : {e}")
