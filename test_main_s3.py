import pytest
from main_s3 import UserController
from main_s3 import GetSpeed
# user_controller = UserController()


@pytest.fixture
def get_started():
    print("starting")
    gs = GetSpeed()
    yield gs
    print("finished")

def test_get_speed(get_started):
    assert get_started.get_speed(100) == "medium"

print("---------------------------------------------")

@pytest.fixture
def user_controller():
    """Create a fresh instance of UserController"""
    controller = UserController()
    yield controller
    controller.database.clear()

def test_add_user(user_controller):
    assert user_controller.add_user(username="jack_brown", email="jack@email.com") == True
    assert user_controller.get_user("jack_brown") == "jack@email.com"


def test_add_duplicate_user(user_controller):
    user_controller.add_user(username="jack_brown", email="jack@email.com")
    with pytest.raises(ValueError):
        user_controller.add_user(username="jack_brown", email="jack@email.com")


def test_delete_user(user_controller):
    user_controller.add_user(username="jack_brown", email="jack@email.com")
    user_controller.delete_user("jack_brown")
    assert user_controller.get_user("jack_brown") is None


