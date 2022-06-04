"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def inverting_the_order_of_the_list_items(list_new, len_of_initial_list):
    if len(list_new) < 2 * len_of_initial_list:
        list_new.insert(len_of_initial_list, (list_new[len(list_new) - len_of_initial_list]))
        return inverting_the_order_of_the_list_items(list_new, len_of_initial_list)
    elif len(list_new) == 2 * len_of_initial_list:
        return "".join(list_new[len_of_initial_list:])
    else:
        pass


list_based_on_the_entered_line_number_one = list(input())


print(inverting_the_order_of_the_list_items(list_based_on_the_entered_line_number_one,
                                            len(list_based_on_the_entered_line_number_one)))

