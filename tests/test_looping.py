from learning import looping


def test_range_loops():
    assert looping.range_loop() == [0, 1, 2, 3, 4]


def test_range_list_comprehension():
    assert looping.range_list_comprehension(5) == [0, 1, 2, 3, 4]
