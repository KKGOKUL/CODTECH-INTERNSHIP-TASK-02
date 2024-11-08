import re

# List of common passwords to check against
common_passwords = ["123456", "password", "12345678", "qwerty", "12345", "abc123", "password1"]

def check_password_strength(password):
    # Initial strength score
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    elif len(password) <= 11:
        score += 1
        feedback.append("Consider using a password longer than 11 characters for better security.")
    else:
        score += 2
        feedback.append("Good length for password.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters to make the password stronger.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters to make the password stronger.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers to make the password stronger.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., @, #, $) to make the password stronger.")

    # Check against common passwords
    if password.lower() in common_passwords:
        score -= 1
        feedback.append("Avoid using common passwords.")

    # Check for simple patterns
    if re.search(r"(.)\1\1", password) or re.search(r"1234|abcd|qwerty", password.lower()):
        score -= 1
        feedback.append("Avoid simple patterns like '1234' or repeated characters.")

    # Provide feedback based on score
    if score >= 5:
        strength = "Strong"
        feedback.append("Password strength is strong.")
    elif score >= 3:
        strength = "Moderate"
        feedback.append("Password strength is moderate.")
    else:
        strength = "Weak"
        feedback.append("Password strength is weak. Consider improving it.")

    return strength, feedback

# Example usage
password = input("Enter a password to check its strength: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
print("Feedback:")
for item in feedback:
    print(f"- {item}")
