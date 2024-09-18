import re

def check_password_strength(password):
    # Initialize strength level
    strength = 0
    
    # Feedback list
    feedback = []
    
    # Check the length of the password
    if len(password) < 4:
        feedback.append("Password is too short (less than 4 characters).")
        strength = 0
    elif len(password) < 8:
        feedback.append("Password length is moderate (between 4 and 7 characters).")
        strength = 1
    else:
        feedback.append("Password length is strong (8 or more characters).")
        strength = 2
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):  # checking for uppercase letters
        feedback.append("Password contains uppercase letters.")
        strength += 1
    else:
        feedback.append("Password does not contain any uppercase letters (consider adding).")
    
    # Check for numbers
    if re.search(r'\d', password):  # checking for digits
        feedback.append("Password contains numbers.")
        strength += 1
    else:
        feedback.append("Password does not contain any numbers (consider adding).")

    # assessment
    if strength <= 1:
        feedback.append("Overall password strength: WEAK.")
        # if the password is weak the user will be asked to retype one
    elif strength == 2 or strength == 3:
        feedback.append("Overall password strength: MODERATE.") 
        # if the passord is longer than 4 character then it is moderate and can be used but it is recomended to use numbers and upper case
    else:
        feedback.append("Overall password strength: STRONG.")
    
    # Return feedback
    return feedback, strength

# Main program with the menu for users
def main():
    while True:
        password = input("Enter your password: ")
        feedback, strength = check_password_strength(password)
        
        # Display feedback
        print("\nPassword Strength Assessment:")
        for line in feedback:
            print(line)

        # If password is weak,it will ask the user to re-enter a stronger password
        if strength <= 1:
            print("\nThe password is too weak. Please choose a stronger password.\n")
        else:
            print("\nPassword is acceptable.")
            break


if __name__ == "__main__":
    main()
