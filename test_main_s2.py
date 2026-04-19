from main_s2 import get_speed
def test_get_speed():
    print("\ntest get speed")
    assert get_speed(80) == "medium"
    # assert get_speed(100) == "high"
