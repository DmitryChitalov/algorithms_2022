"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


def reverse(number):
    reverse_number = ''
    if number >= 10:
        new_number = number // 10
        num = number - new_number * 10
        reverse_number = reverse_number + str(num) + reverse(new_number)
    else:
        reverse_number = str(number)

    return reverse_number

@profile
def func(input_num):
   return reverse(input_num)




if __name__ == '__main__':
    input_num = int(input('Введите число: '))
    print(func(input_num))



"""
Проблема получаем много таблиц, по количеству итераций
Решение - делаем функцию обертку в которой вызываем рекурсию и получаем одну общую таблицу
"""