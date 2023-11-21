import datetime
import pytest


@pytest.fixture
def current_date():
    return datetime.date.today()
