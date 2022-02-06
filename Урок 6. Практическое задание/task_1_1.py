"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""
from pympler import asizeof
import collections
import json
import memory_profiler
from timeit import timeit

""" исходное """
info_store = {
    "poor company": -345.414,
    "negative solutions": -31412515141412,
    "Google vilage": 1324155.3130,
    "Abb": 43431211,
    "Siemens": 116002334.44,
    "Reaktor base": 2030304,
    "Kumara": 5922323.4214,
    "Drama company": 323330314,
    "Komedy Film": 203204124.31,
    "Some other": 12034
}

#@memory_profiler.profile
def get_three_profitable_comp(info_storage) -> dict:
    """
    Задание 3 из урока 1 курса Алгоритмы и структуры данных.
    Задача:
    Имеется хранилище с информацией о компаниях: название и годовая прибыль.
    Для реализации хранилища можно применить любой подход,
    который вы придумаете, например, реализовать словарь.
    Реализуйте поиск трех компаний с наибольшей годовой прибылью.
    Выведите результат.
    Сложность: Т(n) = 2n + 5 => O(n)
    """
    tmp_storage = info_storage.copy()
    max_annual_profit_companies = {}
    for x in range(3):
        company, value = max(tmp_storage.items(), key=lambda x: x[1])
        del tmp_storage[company]
        max_annual_profit_companies.update({company: value})
    return max_annual_profit_companies


""" оптимизированное """
info_store_opt = json.dumps({
    "poor company": -345.414,
    "negative solutions": -31412515141412,
    "Google vilage": 1324155.3130,
    "Abb": 43431211,
    "Siemens": 116002334.44,
    "Reaktor base": 2030304,
    "Kumara": 5922323.4214,
    "Drama company": 323330314,
    "Komedy Film": 203204124.31,
    "Some other": 12034
})

#@memory_profiler.profile
def get_three_profitable_comp_opt(storage: json) -> list:
    """
    Оптимизированая функция, Использование Counter вместо написания дополнительной логики.
    Десиреализация обьекта.
    :param storage: json string
    :return: list
    """
    values = json.loads(storage)
    counter = collections.Counter(values)
    return counter.most_common(3)


if __name__ == "__main__":
    print(f"dict (info_store) size: {asizeof.asizeof(info_store)}")
    print(f'function get_three_profitable_comp executing takes: '
          f'{timeit("get_three_profitable_comp(info_store)", globals=globals(), number=100000)} s')
    #print(get_three_profitable_comp(info_store))

    print(f"serialized object (info_store_opt) size: {asizeof.asizeof(info_store_opt)}")
    print(f'function get_three_profitable_comp_opt executing takes: '
          f'{timeit("get_three_profitable_comp_opt(info_store_opt)", globals=globals(), number=100000)} s')
    #print(get_three_profitable_comp_opt(info_store_opt))


"""
Результаты: 
    dict (info_store) size: 1272
    function get_three_profitable_comp executing takes: 0.5589341 s
    serialized object (info_store_opt) size: 320
    function get_three_profitable_comp_opt executing takes: 1.494539 s
Вывод: 
    Видна разница оптимиризования словаря, против сериализации обьекта в json -> потребление памяти уменьшилось в 4 раза.
    Однако время затраченое на исполнения функции увеличилось почти в 3 раза.
    Затраты памяти не столь велики поэтому профилирование памяти не показало особых результатов.
    
Профилирование памяти:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    53     19.7 MiB     19.7 MiB           1   @memory_profiler.profile
    54                                         def get_three_profitable_comp(info_storage) -> dict:                                   
    65     19.7 MiB      0.0 MiB           1       tmp_storage = info_storage.copy()
    66     19.7 MiB      0.0 MiB           1       max_annual_profit_companies = {}
    67     19.7 MiB      0.0 MiB           4       for x in range(3):
    68     19.7 MiB      0.0 MiB          57           company, value = max(tmp_storage.items(), key=lambda x: x[1])
    69     19.7 MiB      0.0 MiB           3           del tmp_storage[company]
    70     19.7 MiB      0.0 MiB           3           max_annual_profit_companies.update({company: value})
    71     19.7 MiB      0.0 MiB           1       return max_annual_profit_companies



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    88     19.7 MiB     19.7 MiB           1   @memory_profiler.profile
    89                                         def get_three_profitable_comp_opt(storage: json) -> list:
    95     19.7 MiB      0.0 MiB           1       values = json.loads(storage)
    96     19.7 MiB      0.0 MiB           1       counter = collections.Counter(values)
    97     19.7 MiB      0.0 MiB           1       return counter.most_common(3)

"""

