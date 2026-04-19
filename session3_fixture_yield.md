### 📌 Session Information

-   **Video of this session:** [Pytest Tutorial #3 – Fixtures](https://www.youtube.com/watch?v=olGSCnKO8P0)
-   **Official pytest Reference:** [https://docs.pytest.org/en/stable/reference/fixtures.html](https://docs.pytest.org/en/stable/reference/fixtures.html)

* * *

### 📚 Pytest Fixtures – Quick Review Document

#### 1\. What is a Fixture?

-   Fixtures are special functions that provide **setup** and **teardown** logic for your tests.
-   They help avoid repeating the same preparation code in every test.
-   pytest automatically manages fixtures and injects them into your test functions.

#### 2\. How to Define a Fixture

Python

    import pytest
    
    @pytest.fixture
    def get_started():
        print("starting")           # Setup
        return GetSpeed()           # Value returned to the test

#### 3\. Using a Fixture in a Test

Python

    def test_get_speed(get_started):    # Fixture name as parameter
        assert get_started.get_speed(100) == "medium"

#### 4\. Setup + Teardown using yield (Most Important Part)

This is the recommended pattern:

Python

    @pytest.fixture
    def get_started():
        print("starting")           # Setup
        gs = GetSpeed()
        yield gs                    # Value passed to the test
        print("finished")           # Teardown (runs after the test finishes)

> **Rule**: Everything **before** yield → Setup Everything **after** yield → Teardown

#### 5\. Fixture Scopes

### 

Scope controls **how often** a fixture is created.

| Scope | Created Once For | Best Used For |
| --- | --- | --- |
| function | Each test (default) | Complete isolation per test |
| class | Each test class | All tests inside one class |
| module | Each Python file | All tests in one module |
| package | Each package | Package-level resources |
| session | Entire test session | Heavy resources (DB, browser, etc.) |

Example:

Python

    @pytest.fixture(scope="session")
    def db_connection():
        ...

#### 6\. Important Fixture Parameters

### 

-   scope – Controls fixture lifetime
-   params – Parametrize the fixture (run multiple times with different values)
-   autouse=True – Automatically use the fixture for all tests
-   ids – Custom readable names for parametrized fixtures

#### 7\. Best Practices

### 

-   Put shared fixtures in a file named **conftest.py** (pytest discovers it automatically).
-   Use yield for clean teardown.
-   Take advantage of built-in fixtures: tmp\_path, monkeypatch, caplog, request, etc.
-   Choose the right scope to make your tests faster.
-   Keep fixtures focused and reusable.