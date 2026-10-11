from password_checker import check_password


def main():
    print("=== Password Strength Checker ===")
    print("Your password is checked locally, not sent to a server.\n")

    password = input("Enter a password to check: ")

    if not password:
        print("Error: Password cannot be empty.")
        return

    result = check_password(password)

    print(f"\nStrength: {result['strength']}")
    print(f"Checks passed: {result['score']}/{result['total_checks']}")

    print("\n--- Security Checks ---")
    for check, passed in result["checks"].items():
        print(f"{'PASS' if passed else 'FAIL'}: {check}")

    if result["suggestions"]:
        print("\nSuggestions:")
        for suggestion in result["suggestions"]:
            print(f"- {suggestion}")
    else:
        print("\nAll checks passed!")

    print("\nNote: This is a basic heuristic, not a guarantee of password security.")


if __name__ == "__main__":
    main()  