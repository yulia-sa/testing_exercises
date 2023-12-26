import pytest
from functions.level_2.three_first import first


@pytest.mark.parametrize(
    "items,expected_result",
    [
        ([0], 0),
        ([1], 1),
        ([-1], -1),
        ([9999999999], 9999999999),
        ([20, 30, 40], 20)
    ]
)
def test__first__return_first_item_without_default(items, expected_result):
    assert first(items) == expected_result


@pytest.mark.parametrize(
    "items,default,expected_result",
    [
        ([5, 6, 7, 8, 9], 10, 5),
        ([5, 6, 7, 8, 9], None, 5),
        ([5, 6, 7, 8, 9], "NOT_SET", 5),
        ([5, 6, 7, 8, 9], "some_str", 5)
    ]
)
def test__first__return_first_item_with_default(items, default, expected_result):
    assert first(items, default) == expected_result


@pytest.mark.parametrize(
    "items,default,expected_result",
    [
        ([], 0, 0),
        ([], 1, 1),
        ([], -1, -1),
        ([], 9999999999, 9999999999),
        ([], None, None),
        ([], "some_str", "some_str"),
        ([], "", ""),
        (None, None, None),
        (None, 555, 555),
        (False, 7000, 7000)
    ]
)
def test__first__return_default(items, default, expected_result):
    assert first(items, default) == expected_result


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
