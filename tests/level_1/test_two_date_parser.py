import datetime
import pytest
from functions.level_1.two_date_parser import compose_datetime_from


current_date = datetime.date.today()
tomorrow_date = current_date + datetime.timedelta(days=1)


@pytest.mark.parametrize(
    "date_str,"
    "time_str,"
    "expected_result_composed_datetime",
    [
        (
            "not meaningful",
            "18:37",
            datetime.datetime(
                current_date.year,
                current_date.month,
                current_date.day,
                18,
                37,
            )
        ),
        (
            "tomorrow",
            "05:01",
            datetime.datetime(
                tomorrow_date.year,
                tomorrow_date.month,
                tomorrow_date.day,
                5,
                1,
            )
        )
    ]
)
def test__compose_datetime_from(date_str, time_str, expected_result_composed_datetime):
    assert compose_datetime_from(date_str, time_str) == expected_result_composed_datetime
