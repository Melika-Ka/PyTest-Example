### 📌 Session 4 Information

#### 

-   **Video of this session:** Pytest Tutorial #4 – conftest.py
-   **Official pytest Reference (Fixtures):** [https://docs.pytest.org/en/stable/reference/fixtures.html](https://docs.pytest.org/en/stable/reference/fixtures.html)

* * *

### 📚 What is conftest.py and Why Is It So Important?

#### 

One of the most powerful features of pytest is the **conftest.py** file. It acts as a **central hub** for managing fixtures and allows you to share fixtures across multiple test files **without importing them**.

#### Key Features of conftest.py

#### 

-   pytest automatically discovers and loads conftest.py files (no import needed).
-   Any fixture defined in conftest.py becomes available to **all test files** in the same directory and its subdirectories.
-   You can have multiple conftest.py files at different directory levels (hierarchical structure).

**Important Folder Structure Note:**

-   Fixtures defined in a parent conftest.py (higher folder) are available to child folders.
-   Fixtures defined in a child folder are **not** available to the parent folder.
-   If a fixture with the same name exists in multiple levels, the **closer** one (child) takes priority and **overrides** the parent fixture.

* * *

### Project Structure Example

#### 

text

    tests/
    ├── conftest.py                  ← Common fixtures for all tests
    ├── test_user.py
    ├── test_order.py
    └── admin/
        ├── conftest.py              ← Fixtures specific to admin section
        └── test_admin_panel.py

* * *

### Example Code in conftest.py

#### 

Python

    # tests/conftest.py
    import pytest
    
    @pytest.fixture(scope="session")
    def db_connection():
        print("Connecting to database...")
        # Simulate database connection
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

Now, in any test file (e.g., test\_user.py), you can directly use these fixtures:

Python

    # test_user.py
    def test_add_user(user_controller, db_connection):
        assert user_controller.add_user("jack", "jack@email.com") == True

**No import required!** pytest automatically injects the fixtures.

* * *

### Fixture Scopes (Quick Reminder)

#### 

| Scope | Created Once For | Best Used For |
| --- | --- | --- |
| function | Each test (default) | Fully isolated tests |
| class | Each test class | All tests inside one class |
| module | Each Python file | All tests in one module |
| package | Each package | Package level (with \_\_init\_\_.py) |
| session | Entire test session | Heavy resources (DB, browser, etc.) |

> **Note:** Fixtures with higher scope are created first.

* * *

### Best Practices

#### 

-   Put **common and shared** fixtures in the root conftest.py.
-   Create separate conftest.py files for fixtures specific to certain sections of your project.
-   Use autouse=True only when the fixture must run for **all** tests.
-   Take advantage of pytest’s built-in fixtures: tmp\_path, monkeypatch, caplog, etc.
-   To see all available fixtures for a test file:
    
    Bash
    
        pytest --fixtures test_file.py
    
-   To see the setup and teardown plan:
    
    Bash
    
        pytest --setup-plan test_file.py
    

* * *

### Session Summary

#### 

In this session, you learned about the **conftest.py** file, which:

-   Allows sharing fixtures across multiple test files.
-   Reduces code duplication.
-   Makes setup and teardown management easier at the project level.
-   Gives you precise control over when fixtures are created and destroyed using different **scopes**.

conftest.py is one of the main reasons why pytest is more powerful and scalable compared to unittest.