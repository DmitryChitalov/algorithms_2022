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
import pickle
from pympler import asizeof
import memory_profiler

@memory_profiler.profile
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


@memory_profiler.profile
def unique_set_opt(some_string: str) -> bytes:
    hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
                for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
    return pickle.dumps(hash_set)



if __name__ == "__main__":
    test_str = "papapdawdawfawfawfawdawfawafdafsfcwadasdwdawpfjawpofjaicnawpodhajwopdawådplaw"
    test1 = unique_set(test_str)
    test2 = unique_set_opt(test_str)

    print(f"Size of test1: {asizeof.asizeof(test1)}")
    print(f"Size of test2 (pickle obj): {asizeof.asizeof(test2)}")

    """
    Результаты: 
        Size of test1: 404800
        Size of test2: 141768
        
    Вывод: 
        При оптимизации функции метод 'консервирования' pickle показал дополнительное потребление памяти на 
        преобразование результата вычислений функции, однако после консервирования на выходе обьект получался в 2,5 раза 
        меньше. Тоесть можно сделать вывод что на в момент вычислений памяти потребуется больше, чем на хранения 
        информации.  
    
    Профилирование функции: 
    
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        38     31.4 MiB     31.4 MiB           1   @memory_profiler.profile
        39                                         def unique_set(some_string: str) -> set:
        49     31.8 MiB      0.0 MiB          80       hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
        50     31.8 MiB      0.4 MiB        3080                   for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
        51     31.8 MiB      0.0 MiB           1       return hash_set


    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        54     31.8 MiB     31.8 MiB           1   @memory_profiler.profile
        55                                         def unique_set_opt(some_string: str) -> bytes:
        56     32.3 MiB      0.0 MiB          80       hash_set = {hashlib.sha1(some_string[i:j].encode("utf-8")).hexdigest() for i in range(len(some_string))
        57     32.3 MiB      0.4 MiB        3080                   for j in range(i+1, len(some_string)+1) if some_string != some_string[i:j]}
        58     32.6 MiB      0.4 MiB           1       return pickle.dumps(hash_set)
    """