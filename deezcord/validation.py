# validation.py

def is_password_long_enough(password):
    return len(password) >= 8

def is_email_valid(email):
    return "@" in email

def check_username_not_empty(username):
    return bool(username and username.strip())

def do_passwords_match(pass1, pass2):
    return pass1 == pass2

def is_age_valid(age):
    return age >= 18