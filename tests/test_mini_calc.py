from app.mini_calc import MiniCalc
import pytest

class TestMiniCalc:
    def setup_method(self):
        print("se executa la inceput")
        self.calc1 = MiniCalc(3, 5)

    def teardown_method(self):
        print("se executa la final")

    def test_sum(self):
        assert self.calc1.sum() == 8, "sum is not working"

    def test_substraction(self):
        assert self.calc1.substraction() == -2, "substraction is not working"

    def test_multiplication(self):
        assert self.calc1.multiplication() == 15, "multiplication is not working"

    @pytest.mark.skip(reason="work in progress")
    def test_division(self):
        assert self.calc1.division() == 0.6, "division is not working"

    def test_sum_custom(self):
        assert self.calc1.sum_custom(33,77) == 110, "custom sum is not working"

    def test_division_custom(self):
        assert self.calc1.division_custom(22, 2) == 11, "custom division is not working"

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (1, 1, 2),
            (1, 2, 3),
            (5.1, 6, 11.1),
        ]
    )
    def test_sum_custom_param(self, a, b, expected):
        assert self.calc1.sum_custom(a, b) == expected, "custom sum not working"

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (4, 2, 2),
            (6, 2, 3),
            (5, 0, 0),
            (7, 0, 4.1)
        ]
    )
    def test_division_custom_param(self, a, b, expected):
        if b == 0:
            print("ZeroDivisionError = division by zero")
            return "ZeroDivisionError"
        assert self.calc1.division_custom(a, b) == expected, "custom division not working"