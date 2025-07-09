import re

def check_password_strength(password):
    score = 0
    remarks = ""

    if len(password) < 6:
        return "Weak: Password too short"

    # Check for various character types
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 1:
        remarks = "Weak: Use a mix of uppercase, lowercase, digits and symbols"
    elif score == 2:
        remarks = "Moderate: Try adding more variety to strengthen it"
    elif score == 3:
        remarks = "Strong: Could be better with symbols"
    elif score == 4:
        remarks = "Very Strong Password!"
    return remarks


if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)
