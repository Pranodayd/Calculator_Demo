EXPECTED_USERNAME = "admin"
EXPECTED_PASSWORD = "secret123"


def login(username, password):
    """Return True only when both username and password match the expected values."""
    return username == EXPECTED_USERNAME and password == EXPECTED_PASSWORD


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    return a / b
