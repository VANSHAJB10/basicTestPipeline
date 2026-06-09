# Group 1 — Math utilities
import time

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_addition():
    time.sleep(2)
    assert add(3, 4) == 7

def test_subtraction():
    time.sleep(2)
    assert subtract(10, 3) == 7
