# Group 4 — Dict / user utilities
import time

def get_full_name(user):
    return f"{user['first']} {user['last']}"

def is_adult(user):
    return user.get("age", 0) >= 18

def test_full_name():
    time.sleep(2)
    user = {"first": "Jane", "last": "Doe", "age": 30}
    assert get_full_name(user) == "Jane Doe"

def test_is_adult():
    time.sleep(2)
    assert is_adult({"age": 20}) is True
    assert is_adult({"age": 15}) is False
