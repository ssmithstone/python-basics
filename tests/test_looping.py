from learning import looping


def test_range_loops():
    assert looping.range_loop() == [0, 1, 2, 3, 4]


def test_range_list_comprehension():
    assert looping.range_list_comprehension(5) == [0, 1, 2, 3, 4]


def test_empty_list_is_false():
    assert bool([]) == False


def test_non_empty_list_is_true():
    assert bool([1]) == True


def test_size_of_list():
    assert 5 == len([0, 1, 2, 3, 4])


def test_any_of_list_are_true():
    assert True == any([True, True])
    assert True == any([True, False])
    assert False == any([False, False])


def test_all_of_list_are_true():
    assert True == all([True, True])
    assert False == all([True, False])
    assert False == all([False, False])


def test_reverse_list_object():
    assert [3, 2, 1] == list(reversed([1, 2, 3]))
