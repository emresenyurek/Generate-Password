import random
import string
# Function to generate a random password
def generate_password(min_lenght, numbers=True, special_characters=True):
    letters= string.ascii_letters # Set of letters
    digits = string.digits  # Set of digits
    special = string.punctuation # Set of special characters

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_lenght:
        new_character = random.choice(characters)
        password += new_character

        # Check if the generated characters meet the password criteria
        if new_character in digits:
            has_number = True
        elif new_character in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

# Get the minimum length and other preferences from the user
min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to have numbers? (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters? (y/n)? ").lower() == "y"

# Generate and print the password
password = generate_password(min_lenght, has_number, has_special)
print("The generated password is:", password)
