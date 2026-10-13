import pytest

from Calculator import add


def test_add_accepts_integers_and_floats():
    assert add(2, 3) == 5
    assert add(1.5, 2.25) == 3.75


@pytest.mark.parametrize("a, b", [("2", 3), (2, "3"), (None, 3), (2, None)])
def test_add_rejects_non_numeric_inputs(a, b):
    with pytest.raises(TypeError, match="Both arguments must be numbers"):
        add(a, b)