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
def create_lst_sum(n=float(input("Введите количество элементов ряда чисел:")), lst_obj=[], el=1):

    if len(lst_obj) == n:
        def get_sum(lst):
            if len(lst) == 1:
                return lst[0]
            else:
                return lst[0] + get_sum(lst[1:])
        print(f'Количество элементов: {n}, их сумма: {get_sum(lst_obj)}')
        return get_sum(lst_obj)

    lst_obj.append(el)
    create_lst_sum(n, lst_obj, el/-2)


create_lst_sum()