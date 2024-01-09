import pytest
from pytest_lazyfixture import lazy_fixture
from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    "date_str,"
    "time_str,"
    "expected_result_composed_datetime",
    [
        (
            "not meaningful",
            "17:23",
            lazy_fixture("today_datetime_17_23")
        ),
        (
            "tomorrow",
            "17:23",
            lazy_fixture("tomorrow_datetime_17_23")
        )
    ]
)
def test__compose_datetime_from(date_str, time_str, expected_result_composed_datetime):
    assert compose_datetime_from(date_str, time_str) == expected_result_composed_datetime
