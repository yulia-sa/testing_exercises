from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test_compose_datetime_from_any_date(current_date):
    assert compose_datetime_from("not meaningful", "18:37") == datetime.datetime(
        current_date.year,
        current_date.month,
        current_date.day,
        18,
        37,
    )


def test_compose_datetime_from_tomorrow(current_date):
    tomorrow_date = current_date + datetime.timedelta(days=1)
    assert compose_datetime_from("tomorrow", "05:01") == datetime.datetime(
        tomorrow_date.year,
        tomorrow_date.month,
        tomorrow_date.day,
        5,
        1,
    )
