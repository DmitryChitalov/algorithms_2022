from timeit import timeit


def format_concate():
    param = 123
    string = "first " + str(param) + " second"


def format_percent():
    param = 123
    string = "first %s second" % param


def format_format():
    param = 123
    string = "first {} second".format(param)


# читаемость и поддерживаемость
def format_f():
    param = 123
    string = f"first {param} second"


print(timeit("format_concate()", globals=globals()))

print(timeit("format_percent()", globals=globals()))

print(timeit("format_format()", globals=globals()))

print(timeit("format_f()", globals=globals()))

"""
0.33543220000000007
0.31619379999999997
0.37685690000000016
0.22341030000000006
"""
