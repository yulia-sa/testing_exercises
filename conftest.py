import datetime
import pytest


@pytest.fixture
def today_datetime_17_23(hour=17, minute=23):
    current_date = datetime.date.today()
    return datetime.datetime.combine(current_date, datetime.time(hour, minute))


@pytest.fixture
def tomorrow_datetime_17_23(today_datetime_17_23):
    return today_datetime_17_23 + datetime.timedelta(days=1)
