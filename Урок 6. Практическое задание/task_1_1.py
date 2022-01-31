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


from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def reverse(number: int) -> str:
    def recursion_reverse(number):
        if number < 10:
            return [number]

        number, remain = divmod(number, 10)
        return [remain] + recursion_reverse(number)
    
    result_list = recursion_reverse(number)
    result_list_str = [str(num) for num in result_list]
    return ''.join(result_list_str)

@decor
def reverse2(number):
    while True:
        number, remain = divmod(number, 10)
        yield str(remain)
        if number == 0:
            break

# Выполнение заняло 0.62109375 Mib       
# result, mem_diff = reverse(int('123'*150))
# print(f"Выполнение заняло {mem_diff} Mib")

# Выполнение заняло 0.00390625 Mib
gen, mem_diff = reverse2(int('123'*150))
print(f"Выполнение заняло {mem_diff} Mib")