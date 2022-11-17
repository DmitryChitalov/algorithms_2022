"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def income():
    def elements_summ(n, fst_el=1.0, summ=0.0):
        if n == 1:
            return print(f'Сумма элементов = {summ}')
        else:
            if fst_el == 1.0:
                summ = fst_el
            snd_el = fst_el / -2
            summ = summ + snd_el
            # print(f'1st={fst_el}, 2nd={snd_el}, summ={summ}, n={n}')
            fst_el = snd_el
            n = n - 1
            elements_summ(n, fst_el, summ)

    num = int(input('Введите число элементов: '))
    return elements_summ(num)


income()
