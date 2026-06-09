# Group 3 — List utilities
import time
 
def get_max(lst):
    return max(lst)
 
def flatten(lst):
    return [item for sublist in lst for item in sublist]
 
def test_max_value():
    time.sleep(2)
    assert get_max([3, 1, 9, 5]) == 9
 
def test_flatten():
    time.sleep(2)
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
