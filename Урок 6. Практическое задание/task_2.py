"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile
# Задание № 1 урока 2 алгоритмы


@profile
def profile_calculator(count):
    def calculator(count):
        # Базовый случай
        if count == "0":
            print("Выход")
            return count

        else:
            # Шаг рекурсии
            if count == "+":
                number_1 = input(" Введите первое число: ")
                number_2 = input(" Введите второе число: ")
                print(int(number_1) + int(number_2))

            elif count == "-":
                number_1 = input(" Введите первое число: ")
                number_2 = input(" Введите второе число: ")
                print(int(number_1) - int(number_2))
            elif count == "*":
                number_1 = input(" Введите первое число: ")
                number_2 = input(" Введите второе число: ")
                print(int(number_1) * int(number_2))
            elif count == "/":
                number_1 = input(" Введите первое число: ")
                number_2 = input(" Введите второе число: ")
                print(int(number_1) / int(number_2))
            else:
                print("Вы ввели не правильное значение")

        return calculator(input(" Введите операцию (+, -, *, / или 0 для выхода): "))
    i = calculator(input(" Введите операцию (+, -, *, / или 0 для выхода): "))
    return i


profile_calculator(0)

# Аналитика
# Проблема заключаеться в вызове значений, каждый раз когда мы запрашиваем данные и работаем с ними,
# дополнительно вызваеться функция memory_profiler, столько раз сколько мы будем заходить в рекурсию,
# проблема решается если обернуть функцию в фнкцию и уже поверх нее сделать декоратор.