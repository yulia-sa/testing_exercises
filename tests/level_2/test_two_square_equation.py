import pytest
from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,expected_result",
    [
        (1.0, 1.0, 1.0, (None, None)),
        (7.0, 2.0, 3.0, (None, None)),
        (7.11, 2.22, 3.33, (None, None)),
        (7.1111111111, 2.2222222222, 3.3333333333, (None, None)),
        (-7.77, -2.22, -3.33, (None, None)),
        (70000000000.70, 20000000000.20, 30000000000.30, (None, None)),
        (0.2, 0.5, 0.9, (None, None))
    ]
)
def test__solve_square_equation__discriminant_less_0(square_coefficient,
                                                     linear_coefficient,
                                                     const_coefficient,
                                                     expected_result):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected_result


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,expected_result",
    [
        (0.0, 0.0, 0.1, (None, None)),
        (0.0, 0.0, 3.0, (None, None)),
        (0.0000000000, 0.0000000000, 7777777777.7777777777, (None, None)),
        (0.0, 0.0, 3333333333.33, (None, None))
    ]
)
def test__solve_square_equation__no_square_coefficient_no_linear_coefficient(square_coefficient,
                                                                             linear_coefficient,
                                                                             const_coefficient,
                                                                             expected_result):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected_result


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,expected_result",
    [
        (0.0, 2.0, 3.0, (-1.5, None)),
        (0.00000000000, 2.2222222222, 3.3333333333, (-1.5, None)),
        (0.00, 32.00, 12.00, (-0.375, None)),
        (0.00, 5555555555.55, 9999999999.99, (-1.7999999999999998, None))
    ]
)
def test__solve_square_equation__no_square_coefficient_yes_linear_coefficient(square_coefficient,
                                                                              linear_coefficient,
                                                                              const_coefficient,
                                                                              expected_result):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected_result


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,expected_result",
    [
        (2.0, 5.0, 3.0, (-1.5, -1.0)),
        (2.0000000000, 5.0000000000, 3.0000000000, (-1.5, -1.0)),
        (2000.0, 5000.0, 3000.0, (-1.5, -1.0)),
        (2.0, 4.0, 2.0, (-1.0, -1.0))
    ]
)
def test__solve_square_equation__discriminant_more_0(square_coefficient,
                                                     linear_coefficient,
                                                     const_coefficient,
                                                     expected_result):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected_result
