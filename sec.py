import string

def check_password_strength(password):
    # Boolean variables for password properties
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Integer to store password length
    length = len(password)
    
    # List of special characters for reference
    special_chars = list(string.punctuation)
    
    # Check password strength
    if length < 6:
        return "Weak", "Try using at least 6 characters, including numbers and special characters."
    elif has_upper and has_lower and has_digit and has_special:
        return "Strong", "Great job! Your password is strong."
    else:
        return "Medium", "Try adding uppercase letters, numbers, and special characters for a stronger password."

def password_checker():
    password_history = []  # List to store previous passwords
    
    while True:
        password = input("Enter your password: ")
        strength, feedback = check_password_strength(password)
        password_history.append(password)
        
        print(f"Password Strength: {strength}")
        print(feedback)
        
        if strength == "Strong":
            break  # Exit loop if password is strong
    
    print("Password history:", password_history)  # Display entered passwords for reference

# Run the password checker
password_checker()
