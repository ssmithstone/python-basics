from learning import numbers


def test_multiplication():
    assert numbers.multiplication(2, 2) == 4


def test_addition():
    assert numbers.addition(1, 2, 3) == 6


def test_builtin_sum():
    assert sum([1, 2, 3]) == 6


def test_subtract():
    assert numbers.subtract(100, 200) == 100


def test_int_divide():
    answer = numbers.int_divide(10, 2)
    assert (type(answer) is int)
    assert answer == 5


def test_float_divide():
    answer = numbers.float_divide(10, 2)
    assert (type(answer) is float)
    assert answer == 5.0


def test_binary_number():
    assert numbers.binary_number() == 15


def test_hex_number():
    assert numbers.hex_number() == 170


def test_oct_number():
    assert numbers.oct_number() == 7


def test_scientific_number():
    assert numbers.scientific_number() == 10
