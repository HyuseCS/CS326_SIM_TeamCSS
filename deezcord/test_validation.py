# test_validation.py
from validation import *

def test_password_length():
    assert is_password_long_enough("12345678") == True

def test_email_valid():
    assert is_email_valid("test@test.com") == True

def test_username_not_empty():
    assert check_username_not_empty("JohnDoe") == True

def test_passwords_match():
    assert do_passwords_match("password123", "password123") == True

def test_age_valid():
    assert is_age_valid(20) == True