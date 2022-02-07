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

Это файл для пятого скрипта
"""
import hashlib
import json
import pickle
from timeit import timeit
from pympler import asizeof
import memory_profiler

#@memory_profiler.profile
def unique_set(some_string: str) -> set:
    """
    Задание 3 урок 3.
    Определить количество различных (уникальных) подстрок
    с использованием хеш-функции.
    Дана строка S длиной N, состоящая только из строчных латинских букв.
    find unique substrings in string
    :param some_string: str
    :return: set
    """
    hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
                for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
    return hash_set


#@memory_profiler.profile
def unique_set_opt_pickle(some_string: str) -> bytes:
    hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
                for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
    return pickle.dumps(hash_set)


#@memory_profiler.profile
def unique_set_opt_json(some_string: str) -> str:
    hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
                for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
    return json.dumps(list(hash_set))


if __name__ == "__main__":
    test_str = "papapdawdawfawfawfawdawfawafdafsfcwadasdwdawpfjawpofjaicnawpodhajwopdawådplaw"
    test1 = unique_set(test_str)
    test2 = unique_set_opt_pickle(test_str)
    test3 = unique_set_opt_json(test_str)

    print("обьекты идентичны" if test1 == pickle.loads(test2) == set(json.loads(test3)) else "Обьекты различны")
    print(f"Size of test1: {asizeof.asizeof(test1)}")
    print(f'time unique_set: {timeit("unique_set(test_str)", globals=globals(), number=1000)} s\n')

    print(f"Size of test2 (pickle obj): {asizeof.asizeof(test2)}")
    print(f'time unique_set_opt_pickle: {timeit("unique_set_opt_pickle(test_str)", globals=globals(), number=1000)} s\n')

    print(f"Size of test3 (json obj): {asizeof.asizeof(test3)}")
    print(f'time unique_set_opt_json: {timeit("unique_set_opt_json(test_str)", globals=globals(), number=1000)} s\n')

    """
    Результаты: 
        Size of test1: 404800
        time unique_set: 4.0415502 s
        
        Size of test2 (pickle obj): 141768
        time unique_set_opt_pickle: 4.234583300000001 s
        
        Size of test3 (json obj): 125408
        time unique_set_opt_json: 4.541763999999999 s
    Вывод: 
        При оптимизации функции метод dumps 'консервирования' pickle и json показал дополнительное потребление памяти на 
        преобразование результата вычислений функции, однако после консервирования на выходе обьект получался в 2,8-3,2
        раза меньше. Тоесть можно сделать вывод что в момент вычислений памяти потребуется больше, чем на хранение 
        информации.  
        Стоит заметить во всем этом есть свои дополнительные минусы такие как обратное преобразование в изначальный 
        обьект. В случае с json, нужно еще дополнительно преобразовать обьект из set в list и что бы получить 
        изначальный обьект обратно в set. Но это уже специфика задачи
        
        Время выполнения функции не сильно поменялось, примерно на 8% на pickle, 12% на json
    
    Профилирование функции: 
    test1
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        38     31.4 MiB     31.4 MiB           1   @memory_profiler.profile
        39                                         def unique_set(some_string: str) -> set:
        49     31.8 MiB      0.0 MiB          80       hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
        50     31.8 MiB      0.4 MiB        3080                   for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
        51     31.8 MiB      0.0 MiB           1       return hash_set

    test2
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        56     31.5 MiB     31.5 MiB           1   @memory_profiler.profile
        57                                         def unique_set_opt_pickle(some_string: str) -> bytes:
        58     31.9 MiB      0.0 MiB          80       hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
        59     31.9 MiB      0.4 MiB        3080                   for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
        60     32.2 MiB      0.3 MiB           1       return pickle.dumps(hash_set)
        
    test3
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        63     31.5 MiB     31.5 MiB           1   @memory_profiler.profile
        64                                         def unique_set_opt_json(some_string: str) -> str:
        65     31.9 MiB      0.0 MiB          80       hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
        66     31.9 MiB      0.4 MiB        3080                   for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
        67     32.2 MiB      0.3 MiB           1       return json.dumps(list(hash_set))
    """