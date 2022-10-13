# Задание 3.

company = {'1': 435, '2': 46789, '3': 32, '4': 654, '5': 3065332}

# Первый способ:
# сложность O(n*log(n))


def value(it):
    ls_1 = []
    ls = {}
    res = sorted(it, key=it.get, reverse=True)
    for i in res:
        max_1 = it.get(i)
        ls_1.append(max_1)
        ls.setdefault(res[0], ls_1[0])
    return ls
print(value(company))


# Второй способ:
# Сложность O (n**2)

max_2 = {}
while len(max_2) < 1:
    max_value = 0
    for k, v in company.items():
        if max_value < v:
            max_value = v
            key = k
    max_value = company.pop(key)
    max_2.setdefault(key, max_value)
print(max_2)

# Вывод: Первый способ выполняется быстрее из-за функции  sorted(), (O(n*log(n)))
