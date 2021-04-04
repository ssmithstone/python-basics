def multiplication(a, b):
    return a * b


def addition(*args):
    value = 0
    for i in args:
        value = value + i
    return value


def subtract(value, source):
    return source - value


def int_divide(a, b):
    return a // b


def float_divide(a, b):
    return a / b


def binary_number():
    return 0b1111


def hex_number():
    return 0xAA


def oct_number():
    return 0o07


def scientific_number():
    return 1e1
