import pytest

def test_add_user(start_sum_numbers,environment):
    if environment == "qa":
        print("Test is running on QA environment")
    elif environment == "dev":
        print("Test is running on Dev environment")
    elif environment == "sum":
        assert start_sum_numbers(2, 3) is 10
        print("Test is running on sum environment")
    else:
        raise ValueError("--env option is wrong")
