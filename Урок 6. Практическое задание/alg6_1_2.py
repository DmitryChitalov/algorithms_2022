from memory_profiler import profile

# поиск минимального значения для списка. дз 1_2


@profile
def list_value():
    val = list(range(100000))
    min_value = val.pop()
    for number in range(len(val)):
        if number < min_value:
            min_value = number
    del val
    return min_value


list_value()
# После выполнения программы удалили ссылку на список "val" , освободив память -2,8

