from learning import strings


def test_formatting():
    assert strings.formatting("joe") == "hello joe"


def test_placeholder_format_message():
    assert strings.placeholder_format_message("joe") == "hello joe"


def test_index_format_message():
    assert strings.index_format_message("joe") == "hello joe"


def test_args_format_message():
    assert strings.args_format_message('joe', 'block') == "hello joe block"


def test_kargs_old_format_message():
    assert strings.kargs_old_format_message(
        name="joe", surname="block") == "hello joe block"


def test_kargs_format_message():
    assert strings.kargs_format_message(name="joe",
                                        surname="block") == "hello joe block"


def test_kargs_f_format_message():
    assert strings.kargs_f_format_message(name="joe", middleName="joe", surname="block") == "hello joe block"


def test_iterator_over_kargs_format_message():
    assert strings.iterator_over_kargs_format_message(
        name="joe", middleName="james", surname="block") == "hello joe james block"
