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

Это файл для первого скрипта
"""

from hashlib import md5

from memory_profiler import profile


@profile
def get_unique_slices_1(string: str) -> int:
    # Вернуть количество уникальных подстрок
    result_hashes: set = set()
    for i in range(1, len(string)):
        for j in range(len(string)-i+1):
            result_hashes.add(md5(string[j:j+i].encode()).hexdigest())
    return len(result_hashes)

@profile
def get_unique_slices_2(string: str) -> int:
    # Вернуть количество уникальных подстрок
    result_hashes: set = set()
    for i in range(1, len(string)):
        [result_hashes.add(md5(string[j:j+i].encode()).hexdigest()) for j in range(len(string)-i+1)]
    return len(result_hashes)

@profile
def get_unique_slices_3(string: str) -> int:
    # Вернуть количество уникальных подстрок
    result_hashes: set = set()
    for i in range(1, len(string)):
        [result_hashes.add(md5(string[j:j+i].encode()).hexdigest()) for j in range(len(string)-i+1)]
    return len(result_hashes)

if __name__ == "__main__":
    string = "qwetryutpoia;sdfkljhsdf;lkjuoiuodfkgnskmrthkjqweqasdgafrtytjnmbn.nn,m.';ok'op;hjkl"
    print(f'Количество уникальных элементов: {get_unique_slices_1(string)}')
    string_2 = "ewqtryutpoia;sdfkljhsdf;lkjuoiuodfkgnskmrthkjqweqasdgafrtytjnmbn.nn,m.';ok'op;hjkl"
    print(f'Количество уникальных элементов: {get_unique_slices_2(string_2)}')
    string_3 = "ewqtryutpoia;sdfkljhsdf;lkjuoiuodfkgnskmrthkjq"
    print(f'Количество уникальных элементов: {get_unique_slices_3(string_3)}')

    """
        Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        39     17.2 MiB     17.2 MiB           1   @profile
        40                                         def get_unique_slices_1(string: str) -> int:
        41                                             # Вернуть количество уникальных подстрок
        42     17.2 MiB      0.0 MiB           1       result_hashes: set = set()
        43     17.7 MiB      0.0 MiB          82       for i in range(1, len(string)):
        44     17.7 MiB      0.0 MiB        3483           for j in range(len(string)-i+1):
        45     17.7 MiB      0.5 MiB        3402               result_hashes.add(md5(string[j:j+i].encode()).hexdigest())
        46     17.7 MiB      0.0 MiB           1       return len(result_hashes)


    Количество уникальных элементов: 3331
    Filename: /home/blackbird/projects/python/algorithms_2022/Урок 6. Практическое задание/task_1_1.py

    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        48     17.7 MiB     17.7 MiB           1   @profile
        49                                         def get_unique_slices_2(string: str) -> int:
        50                                             # Вернуть количество уникальных подстрок
        51     17.7 MiB      0.0 MiB           1       result_hashes: set = set()
        52     17.7 MiB      0.0 MiB          82       for i in range(1, len(string)):
        53     17.7 MiB      0.0 MiB        3645           [result_hashes.add(md5(string[j:j+i].encode()).hexdigest()) for j in range(len(string)-i+1)]
        54     17.7 MiB      0.0 MiB           1       return len(result_hashes)


    Количество уникальных элементов: 3334
    Filename: /home/blackbird/projects/python/algorithms_2022/Урок 6. Практическое задание/task_1_1.py

    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        56     17.7 MiB     17.7 MiB           1   @profile
        57                                         def get_unique_slices_3(string: str) -> int:
        58                                             # Вернуть количество уникальных подстрок
        59     17.7 MiB      0.0 MiB           1       result_hashes: set = set()
        60     17.7 MiB      0.0 MiB          46       for i in range(1, len(string)):
        61     17.7 MiB      0.0 MiB        1215           [result_hashes.add(md5(string[j:j+i].encode()).hexdigest()) for j in range(len(string)-i+1)]
        62     17.7 MiB      0.0 MiB           1       return len(result_hashes)


    Количество уникальных элементов: 1047

    """

    """
    
    """
