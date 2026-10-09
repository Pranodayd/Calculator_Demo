import pytest

from CalculatorModule import Claculator


class TestCalculatorModule:
    def test_add_two_positive_integers(self):
        calc = Claculator()
        assert calc.add(2, 3) == 5

    def test_add_with_zero(self):
        calc = Claculator()
        assert calc.add(0, 7) == 7
        assert calc.add(7, 0) == 7

    def test_add_negative_numbers(self):
        calc = Claculator()
        assert calc.add(-4, 6) == 2
        assert calc.add(-4, -6) == -10

    def test_add_floats(self):
        calc = Claculator()
        assert calc.add(1.5, 2.25) == 3.75

    def test_add_multiple_calls_on_same_instance(self):
        calc = Claculator()
        assert calc.add(10, 20) == 30
        assert calc.add(5, 5) == 10

    def test_average_empty_list_raises_value_error(self):
        calc = Claculator()
        with pytest.raises(ValueError, match="Cannot compute average of an empty list"):
            calc.average([])

    def test_total_matches_previous_behavior(self):
        calc = Claculator()
        assert calc.total(1, 2, 3, 4) == 10
        assert calc.total(-1, 2, 3, 4) == 8

    def test_max_value_returns_largest_number(self):
        calc = Claculator()
        assert calc.max_value([3, 8, 1, 12, 5]) == 12
        assert calc.max_value([-5, -1, -9, -3]) == -1

    def test_max_value_empty_list_raises_value_error(self):
        calc = Claculator()
        with pytest.raises(ValueError, match="Cannot find the largest number in an empty list"):
            calc.max_value([])
