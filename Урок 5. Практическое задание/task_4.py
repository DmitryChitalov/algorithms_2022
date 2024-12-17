"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

numers = 1000000
# Создание обычного словаря
test_dict = {i: i for i in range(numers)}
# Создание упорядоченного словаря OrderedDict
test_order_dict = OrderedDict({i: i for i in range(numers)})


# Изменения ключа в словаре
def test_modif_dict(in_dict: dict[int, int]) -> None:
    """изменеие ключа"""
    for i in range(numers):
        in_dict[i] = f'{i} updated'
    return None


# Получение значения по ключу в словаре
def test_get_dict(in_dict: dict[int, str]) -> None:
    """получение значения по ключу"""
    for i in range(numers):
        in_dict.get(i)
    return None


# Добавления нового ключа в словаре
def test_add_dict(in_dict: dict[int, str]) -> None:
    """добавление нового ключа"""
    for i in range(numers):
        in_dict[i + numers] = f'{i + numers}'
    return None


# Итерация по словарю
def test_iter_dict(in_dict: dict[int, str]) -> None:
    """итерация по словарю"""
    for key, value in in_dict.items():
        pass  # Просто проходим по всем элементам
    return None


# Тест удаления ключа из словаря
def test_del_dict(in_dict: dict[int, str]) -> None:
    """удаление ключа и значения"""
    for i in range(numers):
        del in_dict[i]
    return None


for func in [test_modif_dict, test_get_dict, test_add_dict, test_iter_dict, test_del_dict]:
    print(f"Тест: {func.__doc__} с обычным словарём: "
          f"{timeit(lambda: func(test_dict), globals=globals(), number=1)} секунд")
    print(f"Тест: {func.__doc__} cо словарём OrderDict: "
          f"{timeit(lambda: func(test_order_dict), globals=globals(), number=1)} секунд")

"""
Выводы:
В OrderedDict все проведённые операции могут быть немного медленнее,
так как порядок элементов должен сохраняться при добавлении,
удалении или изменении элементов в отличии обычного словаря.

Заключение:
В Python 3.6 и более поздних версиях, где обычные словари начали поддерживать порядок добавления элементов,
использование OrderedDict теряет смысл для большинства операций,
если вам не нужен строгий порядок при добавлении/удалении элементов.
Если требуется гарантированное сохранение порядка элементов при всех операциях,
то OrderedDict может быть полезен, но, скорее всего,
это будет иметь небольшое влияние на производительность.
Для большинства сценариев в Python 3.7 и выше обычные словари будут работать так же быстро,
как и OrderedDict, но будут занимать меньше памяти и иметь более простую реализацию.
"""
