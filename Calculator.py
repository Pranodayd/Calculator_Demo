def add(a, b):
    # Return the sum of two numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def is_even():
    # Return all even numbers from 1 to 10
    return [n for n in range(1, 11) if n % 2 == 0]


def greet(name):
    # return a friendly greeting
    return f"Hello, {name}!"
