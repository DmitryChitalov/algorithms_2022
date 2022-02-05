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


from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        print(f"Выполнение заняло {memory_usage()[0] - m1[0]} Mib")
        return res

    return wrapper


def sum_digit(digit):
    result = 0
    while True:
        remainder = digit % 10
        result += remainder
        digit = digit // 10
        if digit <= 0:
            break

    return result


@memory
def before(cube_list):
    result = 0
    for elem in cube_list:
        if sum_digit(elem) % 7 == 0:
            result += elem

    print('Сумма 1:', result)

    result = 0
    for i in range(len(cube_list)):
        cube_list[i] += 17
        if sum_digit(cube_list[i]) % 7 == 0:
            result += cube_list[i]

    print('Сумма 2:', result)


def multiple_seven(elem):
    if sum_digit(elem) % 7 == 0:
        return elem
    else:
        return 0

# оптимизация
@memory
def after(cube_list):
    sum_elem = sum(map(multiple_seven, cube_list))

    print('Сумма 1:', sum_elem)

    sum_elem = list(map(lambda x: x + 17, cube_list))
    sum_elem = sum(map(multiple_seven, sum_elem))
    print('Сумма 2:', sum_elem)


if __name__ == '__main__':
    cube_list = [i ** 3 for i in range(1, 100000, 2)]

    before(cube_list.copy())
    after(cube_list.copy())

"""
Используем 'map'.
Использование map действительно позволяет существенно экономить память. 
До:    Выполнение заняло 2.34375 Mib
После: Выполнение заняло 0.11328125 Mib
"""
