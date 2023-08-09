"""
Module to test the functions
"""
from projectlib.sample import reverse, swap


def test_reverse():
    """
    I am here to test reverse function
    """
    assert "thgiarts" in reverse("straight")


def test_swap():
    """
    I am here to test swap function
    """
    test_first_string = "good"
    test_second_string = "bad"
    assert swap(test_first_string, test_second_string) == ("bad", "good")
