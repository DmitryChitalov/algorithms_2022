"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_odd(num, even=0, odd=0):
    # print(f'num = {num} ,even= {even} , odd= {odd} ')
    num1 = num % 10
    # print(f' num1 = {num1} ,  ', end='')
    if num1 % 2:
        odd += 1
        # print('odd ')
    else:
        even += 1
        # print('even ')
    if num < 10:
        pass
        print('\n Result:')
        print(f'number = {number} ,even= {even} , odd= {odd} ')
        return
    else:
        num = num // 10
        even_odd(num, even, odd)


def digit_input():
    while True:
        try:
            num = int(input(" please enter an INT  number:   "))
            return num
        except ValueError:
            continue


if __name__ == '__main__':
    number = digit_input()
    even_odd(number)

# SCRIPT Listing:
#  please enter an INT  number:   1122334400
#
#  Result:
# number = 1122334400 ,even= 6 , odd= 4
