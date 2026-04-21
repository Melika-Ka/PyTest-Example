from main_s5 import sum_numbers
import pytest

# user_controller = UserController()

def pytest_addoption(parser):
    parser.addoption("--env", default="qa")


@pytest.fixture(scope="session", autouse=True)
def environment(request):
    """Return the environment passed via command line"""
    return request.config.getoption("--env")

@pytest.fixture()
def start_sum_numbers():
    sum = sum_numbers
    yield sum
