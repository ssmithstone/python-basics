def formatting(name):
    return f"hello {name}"


def placeholder_format_message(name):
    return "hello {name}".format(name=name)


def index_format_message(name):
    return "hello {0}".format(name)


def args_format_message(*args):
    return "hello {0} {1}".format(*args)


def kargs_old_format_message(**kargs):
    return "hello %s %s" % (kargs['name'], kargs['surname'])


def kargs_format_message(**kargs):
    return "hello {name} {surname}".format(**kargs)


def kargs_f_format_message(**kargs):
    return f"hello {kargs['name']} {kargs['surname']}"


def iterator_over_kargs_format_message(**kargs):
    message = "hello"
    for value in kargs.values():
        message = f"{message} {value}"
    return message
