import random
import string


def generate_password(length):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))

        password = generate_password(length)

        print(f"Generated password: {password}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()