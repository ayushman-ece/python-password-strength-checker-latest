
import re
import string


def check_password(password):
    checks = {
        "At least 12 characters": len(password) >= 12,
        "Contains an uppercase letter": any(c.isupper() for c in password),
        "Contains a lowercase letter": any(c.islower() for c in password),
        "Contains a number": any(c.isdigit() for c in password),
        "Contains a special character": any(
            c in string.punctuation for c in password
        ),
        "No common repeated sequence": not re.search(
            r"(.)\1{3,}", password
        ),
    }

    score = sum(checks.values())

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    suggestions = [
        message for message, passed in checks.items() if not passed
    ]

    return {
        "strength": strength,
        "score": score,
        "total_checks": len(checks),
        "checks": checks,
        "suggestions": suggestions,
    }
