from werkzeug.security import generate_password_hash, check_password_hash


def encrypt(password):
    return generate_password_hash(password, method='scrypt')


def check_hash(hashedValue, inputValue):
    return check_password_hash(hashedValue, inputValue)
