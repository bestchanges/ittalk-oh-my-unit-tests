import datetime
import time

from freezegun import freeze_time


def calculation():
    # pretend long calculation
    time.sleep(0.5)
    now = datetime.datetime.now()
    return {
        'result': 18,
        'finished': now.strftime("%H:%M:%S")
    }


def test_calculation():
    now = datetime.datetime.now()
    expected = {
        'result': 18,
        'finished': now.strftime("%H:%M:%S"),
    }
    result = calculation()

    # spontaneously fail 50% runs
    assert result == expected





@freeze_time("2010-01-01 12:58:33")
def test_calculation_corrected():
    expected = {
        'result' : 18,
        'finished': '12:58:33'
    }
    result = calculation()
    assert result == expected
