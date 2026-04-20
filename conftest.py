#s4

## content of tests/conftest.py

from main_s4 import UserController
import pytest


@pytest.fixture(scope="session")
def db_connection():
    print("Connecting to database...")
    # شبیه‌سازی اتصال به دیتابیس
    conn = {"status": "connected"}
    yield conn
    print("Closing database connection...")
    # teardown


@pytest.fixture(scope="module")
def user_controller():
    print("Creating UserController...")
    controller = UserController()
    yield controller
    print("Cleaning up UserController...")

##  ====================== Scope Examples S4 ======================

@pytest.fixture(scope="function")   # پیش‌فرض - برای هر تست اجرا می‌شود
def function_fixture():
    print("\n>>> Function scope SETUP")
    yield "function_value"
    print("<<< Function scope TEARDOWN")


@pytest.fixture(scope="module")     # یک بار برای تمام تست‌های این فایل
def module_fixture():
    print("\n>>> Module scope SETUP")
    yield "module_value"
    print("<<< Module scope TEARDOWN")


@pytest.fixture(scope="session")    # یک بار در کل اجرای تست‌ها
def session_fixture():
    print("\n>>> Session scope SETUP")
    yield "session_value"
    print("<<< Session scope TEARDOWN")


@pytest.fixture(scope="class")
def class_fixture():
    print("\n>>> Class scope SETUP")
    yield "class_value"
    print("<<< Class scope TEARDOWN")