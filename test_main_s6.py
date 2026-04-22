import pytest
from main_s2 import get_speed


@pytest.mark.skip
def test_get_speed():
    print("Test 3")
    assert get_speed(90) == "medium"


@pytest.mark.xfail
def test_get_speed_slow():
    print("\nTest 4")
    assert get_speed(20) == "medium"

@pytest.mark.smoke
def test_get_speed():
    print("Test 1")
    assert get_speed(90) == "medium"


@pytest.mark.regression
@pytest.mark.smoke
def test_get_speed_slow():
    print("Test 2")
    assert get_speed(20) =="low"