import string
import getpass

def check_password():
    password = getpass.getpass("Enter your password: ")
    strength = 0
    remarks = ''

    lower_count = sum(1 for c in password if c.islower())
    upper_count = sum(1 for c in password if c.isupper())
    num_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if c in string.punctuation)

    strength += bool(lower_count)
    strength += bool(upper_count)
    strength += bool(num_count)
    strength += bool(special_count)

    remarks_dict = {
        1: "Very Bad Password!!! Change ASAP",
        2: "Not a good password!!! Change ASAP",
        3: "It's a weak password, consider changing",
        4: "It's a hard password, can be better",
        5: "A very Strong Password"
    }

    remarks = remarks_dict.get(strength, "Unable to evaluate password")

    print("\nYour password contains: ")
    print(f" {lower_count} lowercase character")
    print(f" {upper_count} uppercase character")
    print(f" {num_count} numeric character")
    print(f" {special_count} special character")

    print(f"\nPassword Strength: {strength}/5")
    print(f"Hint: {remarks}\n")

def ask_to_continue(prompt):
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'. ")


if __name__ == '__main__':
    print("+++ Welcome to the password strength checker +++\n")
    while ask_to_continue("Do you want to check password"):
        check_password()