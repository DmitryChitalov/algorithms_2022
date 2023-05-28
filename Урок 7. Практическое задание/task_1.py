"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
import random
import timeit


def bubblesort(data: list[int]) -> list[int]:
    trigger = False
    while trigger == False:
        trigger = True
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                trigger = False
                tmp = data[i+1]
                data[i+1] = data[i]
                data[i] = tmp

    return data

def revbubblesort(data: list[int]) -> list[int]:
    trigger = False
    span = len(data) - 1
    while span != 0 and trigger == False:
        trigger = True
        for i in range(span):
            if data[i] < data[i + 1]:
                trigger = False
                tmp = data[i + 1]
                data[i + 1] = data[i]
                data[i] = tmp
        span = span - 1

    return data


def revbubblesortslow(data: list[int]) -> list[int]:
    """

    :param data:
    :return:
    """
    span = len(data)-1
    while span !=0:
        for i in range(span):
            if data[i] < data[i+1]:
                tmp = data[i+1]
                data[i+1] = data[i]
                data[i] = tmp
        span = span - 1

    return data


if __name__ == "__main__":
    random.seed()
    inputdata = []
    for i in range(100):
        inputdata.append(random.randint(-100,100))
    print(inputdata)
    print(revbubblesort(inputdata[:]))
    print(revbubblesortslow(inputdata[:]))
    a = lambda: revbubblesort([random.randint(-100,100) in range(100)])
    b = lambda: revbubblesortslow([random.randint(-100,100) in range(100)])
    print(timeit.timeit(a, number=1000))
    print(timeit.timeit(b, number=1000))
    # Доработка эффективна везде за исключением тех случаев где массив не содержит отсортированных подмножеств
