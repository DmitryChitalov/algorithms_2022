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

from memory_profiler import profile

# задание из первого урока курса основ:
# Вычислить сумму кубов нечётных чисел от 1 до 1000 (ниже 10000 - искусственный инкремент),
# сумма цифр которых делится нацело на 7

@profile
def shell():
    number_list = []
    for i in range(1, 100000, 2):
        number_list.append(i ** 3)

    numbers_summ = 0
    for number in number_list:
        number_copy = number
        figure_summ = 0
        while number_copy > 0:
            figure_summ += number_copy % 10
            number_copy = number_copy // 10
        if figure_summ % 7 == 0:
            numbers_summ += number
    print('Сумма чисел из списка, сумма цифр которых делится нацело на 7 =', numbers_summ)

# оптимизируем программу используя генератор вместо списка bumber_list, замеры подтверждают экономию памяти

@profile
def shell_2():
    def number_list():
        for i in range(1, 100000, 2):
            yield i ** 3

    numbers_summ = 0
    for number in number_list():
        number_copy = number
        figure_summ = 0
        while number_copy > 0:
            figure_summ += number_copy % 10
            number_copy = number_copy // 10
        if figure_summ % 7 == 0:
            numbers_summ += number
    print('Сумма чисел из списка, сумма цифр которых делится нацело на 7 =', numbers_summ)


shell()
shell_2()
