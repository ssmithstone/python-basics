def range_loop():
    values = []
    for v in range(5):
        values.append(v)
    return values


def range_list_comprehension(size):
    return [x for x in range(size)]
