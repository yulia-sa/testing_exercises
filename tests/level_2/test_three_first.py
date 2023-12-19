import pytest
from functions.level_2.three_first import first


def test__first__return_first_item():
    NOT_SET = "NOT_SET"

    assert first([0]) == 0
    assert first([1]) == 1
    assert first([-1]) == -1
    assert first([9999999999]) == 9999999999
    assert first([20, 30, 40]) == 20
    assert first([5, 6, 7, 8, 9], 10) == 5
    assert first([5, 6, 7, 8, 9], None) == 5
    assert first([5, 6, 7, 8, 9], NOT_SET) == 5
    assert first([5, 6, 7, 8, 9], "some_str") == 5


def test__first__return_attr_err_on_default_not_set():
    NOT_SET = "NOT_SET"

    with pytest.raises(AttributeError):
        first([])

    with pytest.raises(AttributeError):
        first(None)

    with pytest.raises(AttributeError):
        first(False)

    with pytest.raises(AttributeError):
        first([], NOT_SET)

    with pytest.raises(AttributeError):
        first(None, NOT_SET)

    with pytest.raises(AttributeError):
        first(False, NOT_SET)

    with pytest.raises(AttributeError):
        first([], "NOT_SET")


def test__first__return_default():
    assert first([], 0) == 0
    assert first([], 1) == 1
    assert first([], -1) == -1
    assert first([], 9999999999) == 9999999999
    assert first([], None) is None
    assert first([], "some_str") == "some_str"
    assert first([], "") == ""
    assert first(None, None) is None
    assert first(None, 555) == 555
    assert first(False, 7000) == 7000
