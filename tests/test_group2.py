# Group 2 — String utilities
import time

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def test_reverse():
    time.sleep(2)
    assert reverse_string("hello") == "olleh"

def test_palindrome():
    time.sleep(2)
    assert is_palindrome("racecar") is True
