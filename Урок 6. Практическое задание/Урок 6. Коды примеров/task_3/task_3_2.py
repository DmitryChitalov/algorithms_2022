import gc


def new_func():
    new_lst = [1, 2, 3]
    new_lst.append(new_lst)
    return new_lst


print(new_func())


obj = gc.collect()
print("Количество скрытых объектов, собранных GC:", obj)
# -> Количество скрытых объектов, собранных GC: 1
