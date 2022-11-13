from memory_profiler import profile

@profile
def func():
    def calc():
        res = input("Введите операцию (+, -, *, / или 0 для выхода): ")
        if res not in ('+', '-', '*', '/', '0'):
            return print("Неизвестная операция"), calc()
        if res == '0':
            return print("Вы вышли из калькулятора")
        try:
            num_1 = int(input('Введите первое число: '))
            num_2 = int(input('Введите второе число: '))
        except ValueError:
            return print("Ошибка: Введите число!"), calc()

        if res == '+':
            return print(f'Ваш результат {num_1 + num_2}'), calc()
        elif res == '-':
            return print(f'Ваш результат {num_1 - num_2}'), calc()
        elif res == '*':
            return print(f'Ваш результат {num_1 * num_2}'), calc()
        elif res == '/' and num_2 != 0:
            return print(f'Ваш результат {num_1 / num_2}'), calc()
        try:
            num_1 / 0
        except ZeroDivisionError:
            return print("На 0 делить нельзя"), calc()
    return calc()
func()

'''
Так как функция рекурсивная, то количество таблиц с замерами соответствует количеству вызовов
Что бы получить одну таблицу с общим замером, оборачиваем функцию другой функцией и её уже замеряем.
'''
