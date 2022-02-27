"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile
""" При профилирование памяти в рекурсивной функции возникает проблема множественного вывода таблиц, на каждый запуск 
функции. Решить эту проблему может оборачивание рекурсивной функции функцией и тогда таблица будет одна с показателями 
по всей рекурсивной функции"""

@profile()
def wrap(nums):
    def count_parity(nums, even=0, not_even=0):
        if nums == 0:  # с базового случая начнется разворот
            return even, not_even  # возвращаем счетчики
        else:
            num = nums % 10  # отделяем число
            nums = nums // 10  # от исходного окалываем последнее число

            if num % 2 == 0:  # если четное, то прибавляем к четному счетчику
                even += 1
            else:  # если не четное, то не к четному
                not_even += 1

            return count_parity(nums, even, not_even)  # вызываем функцию с другими даными
    return count_parity(nums)

print(wrap(int(input())))