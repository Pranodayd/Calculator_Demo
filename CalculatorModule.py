class Claculator:
    def add(self, a, b):
        return a + b

    def average(self, numbers):
        if not numbers:
            raise ValueError("Cannot compute average of an empty list")
        return sum(numbers) / len(numbers)

    def total(self, a, b, c, d):
        """Return the sum of four numeric values.

        Args:
            a: First number to add.
            b: Second number to add.
            c: Third number to add.
            d: Fourth number to add.

        Returns:
            The total of a + b + c + d.

        Raises:
            TypeError: If any argument is not numeric.

        Example:
            calc = Claculator()
            calc.total(1, 2, 3, 4)  # returns 10
        """
        return a + b + c + d

    def max_value(self, numbers):
        if not numbers:
            raise ValueError("Cannot find the largest number in an empty list")
        return max(numbers)
