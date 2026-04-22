# Pytest – Session 6: Working with Markers

### 

This session (based on [YouTube video](https://www.youtube.com/watch?v=0JjzDk2xAqY)) focuses on **Pytest markers**, which allow developers to categorize and manage tests easily.

Markers are useful for skipping, expecting failures, and grouping tests for selective execution.

* * *

## 🔹 What Are Markers?

### 

Markers are annotations (decorators) you can apply to test functions in Pytest.

They begin with `@pytest.mark.<name>` and modify test behavior or classification.

* * *

## 🔸 Built‑in Markers

### 1\. `@pytest.mark.skip`

### 

Skips the test completely — Pytest will not execute it.

```py
@pytest.mark.skip 
def test_example_skip():     
    assert True
 ```

The output will show the test as **skipped** in the results.

* * *

### 2\. `@pytest.mark.xfail`

### 

Marks a test as **expected to fail**.

If the test fails, it won’t be considered an error.

If it passes unexpectedly, Pytest will note it as **XPASS**.


`@pytest.mark.xfail def test_expected_to_fail():     assert 1 == 2`

* * *

### Example from Session

### 


```py
import pytest from main 
import get_speed  
@pytest.mark.skip 
def test_get_speed():     
    print("Test 3")     
    assert get_speed(90) == "fast"  
@pytest.mark.xfail 
def test_get_speed_slow():    
    print("Test 4")     
    assert get_speed(20) == "slow"
 ```

Here:

-   First test is **skipped**
-   Second test is **expected to fail** (for demonstration)

* * *

## 🔸 Custom Markers

### 

You can define your own markers to organize different types of tests such as **smoke**, **regression**, **integration**, etc.

Example:

```py
import pytest from main import get_speed  
@pytest.mark.smoke 
def test_get_speed():     
    print("Test 1")     
    assert get_speed(90) == "fast"  
@pytest.mark.regression 
@pytest.mark.smoke 
def test_get_speed_slow():     
    print("Test 2")     
    assert get_speed(20) == "slow"
```

* * *

## 🏷 Using Custom Markers from Command Line

### 

To run only tests with a specific marker:

`pytest -m smoke`

To exclude a marker:


`pytest -m "not regression"`

* * *

## ⚙️ Registering Custom Markers (optional but recommended)

### 

You should register your custom markers in `pytest.ini`:


`[pytest] markers =     smoke: quick validation tests     regression: detailed regression tests`

This avoids warnings from pytest about “unknown markers.”

* * *

## 🧭 Summary

### 

| Marker | Purpose | Example |
| --- | --- | --- |
| `skip` | Prevents the test from running | `@pytest.mark.skip` |
| `xfail` | Marks a test expected to fail | `@pytest.mark.xfail` |
| Custom (`smoke`, `regression`, etc.) | Organizes categories of tests | `@pytest.mark.smoke` |

* * *

**References:**

-   Official Pytest Docs: [https://docs.pytest.org/en/stable/example/markers.html](https://docs.pytest.org/en/stable/example/markers.html)
-   Session Source: [YouTube Video](https://www.youtube.com/watch?v=0JjzDk2xAqY)