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

Это файл для второго скрипта
"""
import re
from memory_profiler import memory_usage


def decor_mem_usage(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@decor_mem_usage
def log_pars(file_path):
    log = []
    pattern = r'^([\d\.]*).*\[([\w\/: +]*)\] \"(\w*)\s([\/\w]*)[^\"]*[\"]\s(\d*)\s(\d*)'
    re_pattern = re.compile(pattern)
    with open(file_path) as f:
        for line in f:
            log.append(re_pattern.findall(line))
    return log


@decor_mem_usage
def log_pars_new(file_path):
    log = ''
    pattern = r'^([\d\.]*).*\[([\w\/: +]*)\] \"(\w*)\s([\/\w]*)[^\"]*[\"]\s(\d*)\s(\d*)'
    re_pattern = re.compile(pattern)
    for line in open(file_path):
        log = log + '\n' + str(re_pattern.findall(line))

    return log


if __name__ == '__main__':
    log, mem_diff = log_pars(r'E:\course\GB\python\basic python\file\nginx_logs.txt')
    print(mem_diff)  # 30.04
    log, mem_diff = log_pars_new(r'E:\course\GB\python\basic python\file\nginx_logs.txt')
    print(mem_diff)  # 4.71

"""
Оптимизация проведена по памяти вместо списка использована строка, но при этом
сильно пострадало быстродействие
"""
