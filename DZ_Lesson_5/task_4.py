import collections, timeit

just_dict = {}
ord_dict = collections.OrderedDict()


def j_d():
    just_dict["a"] = 1
    print(just_dict["a"])
    print(just_dict.keys())
    just_dict.clear()


def o_d():
    ord_dict["a"] = 1
    print(ord_dict["a"])
    print(ord_dict.keys())
    just_dict.clear()


one = timeit.timeit("j_d()", setup="from __main__ import j_d", number=1000)
two = timeit.timeit("o_d()", setup="from __main__ import o_d", number=1000)

print(one)
print(two)

# orderdict всегда тратит больше времени чем обычный словарь (думаю из-за того что orderdict хранит порядок по другому)
