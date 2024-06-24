def check_password_strength(password):
    # Define special characters
    special_chars = set("!@#$%&*")
    
    # Check for digits, lowercase, uppercase, and special characters
    isdigit_there = any(char.isdigit() for char in password)
    islower_there = any(char.islower() for char in password)
    isupper_there = any(char.isupper() for char in password)
    special_char_there = any(char in special_chars for char in password)
    
    # Check if all criteria are met
    all_true = all([isdigit_there, isupper_there, special_char_there, islower_there])
    
    # Determine password strength
    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and all_true:
        return "Strong"
    else:
        return "Average"

# Get user input for password
input_password = input("Create Password: ")
strength = check_password_strength(input_password)

# Print the password strength
print(f"\nYour password is {strength}!")
