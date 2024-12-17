"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

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

Это файл для третьего скрипта
Задание взял из Урок 3, task_3.
"""

"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib
import itertools
from timeit import timeit

from memory_profiler import memory_usage


def count_memory_usage(func):
    def wrapper(*args, **kwargs):
        mem_before = memory_usage()[0]
        print(f'Время выполнения: {timeit(lambda: func(*args, **kwargs), number=100000)} секунд')
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию с параметрами.
        print(f'Использовано памяти: {memory_usage()[0] - mem_before} MiB')
        return result

    return wrapper


str_obj = "рара"


# Декорируем функцию для подсчета используемой памяти и времени выполнения.
@count_memory_usage
def get_unique_substrings(str_obj: str) -> int:
    unique_hashes = set()
    N = len(str_obj)
    # Перебираем все возможные подстроки.
    for i in range(N):
        for j in range(i + 1, N + 1):
            substring = str_obj[i:j]
            # Проверяем является ли это подстрокой.
            if substring != str_obj:
                # Вычисляем хеш подстроки (используем hashlib для надежного хеширования).
                hash_value = hashlib.sha256(substring.encode('utf-8')).hexdigest()
                if hash_value not in unique_hashes:
                    # print(substring)
                    unique_hashes.add(hash_value)
    return len(unique_hashes)


# print(f"{str_obj} - {get_unique_substrings(str_obj)}  уникальных подстрок")

@count_memory_usage
def unique_substrings_count(S: str) -> int:
    unique_hashes = set()  # Множество для хранения уникальных хешей подстрок.
    N = len(S)

    # Генерация всех возможных подстрок с помощью itertools.combinations.
    for i, j in itertools.combinations(range(N + 1), 2):
        substring = S[i:j]
        # Проверяем является ли это подстрокой.
        if substring != S:
            # Если это часть слова, а не слово целиком.
            # Вычисляем хеш подстроки (используем hashlib для надежного хеширования).
            hash_value = hashlib.sha256(substring.encode('utf-8')).hexdigest()
            if hash_value not in unique_hashes:
                # print(substring)
                unique_hashes.add(hash_value)

    return len(unique_hashes)


# Запуск оригинальной и оптимизированной версий.
get_unique_substrings(str_obj)
unique_substrings_count(str_obj)
"""
Использование memory_profiler позволило увидеть, что функция combinations из модуля itertools
занимает значительно меньше памяти для генерации подстрок,
и незначительно снижает время выполнения.
"""
