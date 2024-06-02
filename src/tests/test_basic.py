from src.funcs import  *

def test_first():
    assert sum([1,2,3]) == 6

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-2) is False


