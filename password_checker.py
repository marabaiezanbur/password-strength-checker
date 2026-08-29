import string


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
    "abc123",
}


def has_repeated_characters(password: str) -> bool:
    """Check if the password contains 3 repeated characters in a row."""
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False


def score_password(password: str) -> tuple[int, str, list[str]]:
    """
    Calculate the strength of a password.

    Returns:
        score: Password score from 0 to 100.
        level: Password strength level.
        suggestions: List of improvement suggestions.
    """

    if not isinstance(password, str):
        return 0, "Very Weak", ["Password must be a text value."]

    if not password:
        return 0, "Very Weak", ["Password is required."]

    score = 0
    suggestions = []

    length = len(password)

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # -------------------------
    # Length
    # -------------------------

    if length < 8:
        score += length * 2
        suggestions.append("Use at least 8 characters.")
    else:
        score += min((length - 7) * 4, 40)

    # -------------------------
    # Character types
    # -------------------------

    if has_lower:
        score += 15
    else:
        suggestions.append("Add lowercase letters.")

    if has_upper:
        score += 15
    else:
        suggestions.append("Add uppercase letters.")

    if has_digit:
        score += 15
    else:
        suggestions.append("Add numbers.")

    if has_special:
        score += 15
    else:
        suggestions.append("Add special characters like !@#$%^&*().")

    # -------------------------
    # Common password detection
    # -------------------------

    if password.lower() in COMMON_PASSWORDS:
        score -= 30
        suggestions.append("Avoid common passwords.")

    # -------------------------
    # Repeated character detection
    # -------------------------

    if has_repeated_characters(password):
        score -= 10
        suggestions.append(
            "Avoid repeating the same character multiple times."
        )

    # -------------------------
    # Bonus
    # -------------------------

    unique_types = sum(
        [
            has_lower,
            has_upper,
            has_digit,
            has_special,
        ]
    )

    if unique_types >= 3 and length >= 12:
        score += 10

    if unique_types == 4 and length >= 16:
        score += 5

    # Keep score between 0 and 100

    score = max(0, min(score, 100))

    # -------------------------
    # Password level
    # -------------------------

    if score >= 85:
        level = "Very Strong"

    elif score >= 65:
        level = "Strong"

    elif score >= 40:
        level = "Medium"

    elif score >= 20:
        level = "Weak"

    else:
        level = "Very Weak"

    if not suggestions:
        suggestions.append("Great password structure.")

    return score, level, suggestions


def display_result(score: int, level: str, tips: list[str]) -> None:
    """Display password analysis results."""

    print("\n" + "=" * 38)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 38)

    print(f"\nScore: {score}/100")
    print(f"Level: {level}")

    print("\nTips:")

    for tip in tips:
        print(f"- {tip}")

    print("\n" + "=" * 38)


def main() -> None:
    print("=" * 38)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 38)

    password = input("\nEnter your password: ")

    score, level, tips = score_password(password)

    display_result(score, level, tips)


if __name__ == "__main__":
    main()