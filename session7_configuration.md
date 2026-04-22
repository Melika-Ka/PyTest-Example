# Session 7 – Global Configuration in Pytest (Using `pytest.ini`)

In this session, we learn how to configure **pytest globally** for a project using a special configuration file. Instead of passing options every time on the command line, we can store them in a config file so that pytest picks them up automatically whenever we run `pytest`.

---

## 1. Why Use a Configuration File?

When projects grow, you often need to:

- Define **custom markers** (e.g. `smoke`, `regression`)
- Change **test file naming patterns**
- Restrict pytest to look for tests in specific **directories**
- Configure **xfail** behavior
- Add **default command-line options** (like `-ra`, `-q`, `-vv`, etc.)

Doing all of this via command-line flags quickly becomes repetitive and error‑prone:

```bash
pytest -m "smoke" -ra -q tests/
```

Instead, you can move these defaults into a config file, and then simply run:

```bash
pytest
```

Pytest will automatically read the configuration and apply it.

---

## 2. Supported Configuration Files

Pytest can read configuration from several file types in your project root:

1. `pytest.ini`
2. `tox.ini`
3. `setup.cfg`
4. `pyproject.toml`

In this session, we focus on **`pytest.ini`**, which is straightforward and widely used.

---

## 3. Basic Structure of `pytest.ini`

A minimal `pytest.ini` file looks like this:

```ini
[pytest]
; configuration options go here
```

Example from our session:

```ini
[pytest]

markers =
    smoke: When passed, it will run tests with smoke tag
    regression: Run regression test

xfail_strict = true

; testpaths = tests

python_files = spec_*.py
```

---

## 4. Defining Custom Markers

Markers are a powerful way to categorize and select tests.

Example:

```python
import pytest

@pytest.mark.smoke
def test_homepage_loads():
    assert True

@pytest.mark.regression
def test_user_can_reset_password():
    assert True
```

To avoid warnings, define them in `pytest.ini`:

```ini
[pytest]
markers =
    smoke: When passed, it will run tests with smoke tag
    regression: Run regression test
```

Run marker groups:

```bash
pytest -m smoke
pytest -m regression
pytest -m "smoke or regression"
pytest -m "smoke and not regression"
```

---

## 5. Configuring `xfail` Behavior (`xfail_strict`)

Example:

```python
import pytest

@pytest.mark.xfail(reason="Bug not fixed yet")
def test_known_bug():
    assert 1 == 2
```

Config:

```ini
xfail_strict = true
```

Behavior:

- Expected fail → `XFAIL`
- Unexpected pass → `XPASS(strict)` → treated as failure

---

## 6. Controlling Test Discovery

### testpaths

```ini
testpaths = tests
```

Pytest will search for tests only inside the `tests` directory.

### python_files

```ini
python_files = spec_*.py
```

Example recognized files:

- `spec_user.py`
- `spec_api.py`
- `spec_login.py`

Multiple patterns:

```ini
python_files = test_*.py spec_*.py *_test.py
```

---

## 7. Full Example

```ini
[pytest]

markers =
    smoke: When passed, it will run tests with smoke tag
    regression: Run regression test

xfail_strict = true

; testpaths = tests

python_files = spec_*.py
```

---

## 8. Example Project Structure

```
my_project/
├─ src/
│  └─ app.py
├─ tests/
│  ├─ spec_auth.py
│  └─ spec_profile.py
└─ pytest.ini
```

Example test:

```python
import pytest

@pytest.mark.smoke
def test_login_page_loads():
    assert True

@pytest.mark.regression
def test_invalid_login_shows_error():
    assert "error" in "error message"

@pytest.mark.xfail(reason="Feature not implemented yet")
def test_login_with_social_account():
    assert False
```

Run tests:

```bash
pytest
pytest -m smoke
pytest -m regression
```

---

## 9. Summary

In this session we learned:

- How to configure pytest globally with `pytest.ini`
- How to define custom markers
- How `xfail_strict` works
- How to control test discovery

Using configuration files keeps test settings consistent across developers and CI environments.
