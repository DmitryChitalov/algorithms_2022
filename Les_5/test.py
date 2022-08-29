from timeit import timeit
dict_dict = {}
for i in range(100):
    dict_dict[i] = i ** 2

dict_dict.pop(90)
print(dict_dict)


def del_key_dict(key):
    dict_dict.pop(key)
    return dict_dict

print(del_key_dict(70))

print(timeit('del_key_dict(25)', globals=globals(), number=10000))