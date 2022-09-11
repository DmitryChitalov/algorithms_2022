"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


@profile
def test_recurs_profile(num):
    def culc_even_noteven(number, even=0, not_even=0):
        """
        Подсчет четных и не четных цифр в цисле
        :param number: введенное цисло
        :param even: количество четных
        :param not_even: количество не четных
        :return: строка с указанием сколько четных и не четных цифр
        """
        if number == 0:
            return f'четных чисел {even}, не четных {not_even}'
        else:
            cur_number = number % 10
            number = number // 10
            if cur_number % 2 == 0:
                even += 1
            else:
                not_even += 1
            return culc_even_noteven(number, even, not_even)

    return culc_even_noteven(num)


if __name__ == '__main__':
    my_num = 2345678
    print(test_recurs_profile(my_num))

    """
    Без обертки в другую функцию на каждый вызов рекурссии создается отдельная таблица profile.
    При обертки в функцию вся статистика объединяется в одну таблицу
    """
