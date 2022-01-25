def first_find_func(lib: dict):
    x = list(lib.values())  # O(N)
    x.sort()  # O(N*log(N))
    x = x[-3:]  # т к в условии задачи топ-3 то сложность O(1)
    for key in lib.keys():  # O(N)
        if lib[key] in x:  # O(1)
            print(key, lib[key])
# Итоговая: O(N*log(N)) - у sort высокая сложность поэтому на больших данных-не вариант
# также отсортированы не по порядку, но условия упорядочивания не было


def sec_find_func(lib: dict):
    x = list(library.values())  # O(N)
    for i in range(3):  # O(1)
        y = max(x)  # O(N)
        x.remove(y)  # O(N)
        for key in lib.keys():  # O(N)
            if lib[key] == y:
                print(key, lib[key])
# Итоговая - O(N) - лучше, чем предыдущий вариант + сортировка по порядку


library = {'reebok': 5000, 'nike': 3000, 'adidas': 8000, 'demix': 1200,
           'ecco': 3500, 'umbro': 2400}
first_find_func(library)
sec_find_func(library)
