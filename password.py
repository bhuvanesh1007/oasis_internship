import random
import string

def generate_password(length=12):
    """Generate a random password.

    Args:
        length (int): Length of the password. Defaults to 12.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to generate and display a password."""
    try:
        password_length = int(input("Enter the length of the password (default is 12): "))
        if password_length <= 0:
            raise ValueError("Password length should be a positive integer.")
    except ValueError:
        print("Invalid input. Using default password length of 12.")
        password_length = 12

    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
