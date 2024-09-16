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


def even_odd_count():
    user_number = abs(int(input('Введите число: ')))

    def even_odd(n, even=0, odd=0):
        if n // 10 == 0:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
            return print(f'Количество четных цифр в числе: {even}, a нечетных: {odd}')
        else:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
            n = n // 10
        return even_odd(n, even, odd)

    return even_odd(user_number)


even_odd_count()


# Переделка
# Спасибо за разбор! Меня расклинило)
def even_odd_count():
    user_number = abs(int(input('Введите число: ')))

    def even_odd(n, even=-1, odd=0):
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

        if n < 1:
            return print(f'Количество четных цифр в числе: {even}, a нечетных: {odd}')
        return even_odd(n // 10, even, odd)

    return even_odd(user_number)


even_odd_count()


"""
Задание 5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
Пример:
32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 
Решите через рекурсию. Решение через цикл не принимается.
Допускается исп-е встроенных ф-ций
"""


def ascii_table(start, finish, row_len, get_row_len=0):
    get_row_len += 1
    if start == finish:
        return print(str(start) + ' - ' + chr(start))
    if get_row_len % row_len != 0:
        return print(str(start) + ' - ' + chr(start), end=' '), ascii_table(start+1, finish, row_len, get_row_len)
    else:
        return print(str(start) + ' - ' + chr(start)), ascii_table(start+1, finish, row_len, get_row_len)


ascii_table(32, 127, 10)


# Переделка
# Я делала дублирования потому, что в примере не было большого разыва между строками при выводе как при использовании
# print('\n'), думала это важный критерий. Ну и до заглушки ретурн тру не додумалась)
def ascii_table(start, finish, row_len, get_row_len=0):
    get_row_len += 1
    if start == finish+1:
        return True

    print(str(start) + ' - ' + chr(start), end=' ')

    if get_row_len % row_len == 0:
        print('\n')

    return ascii_table(start + 1, finish, row_len, get_row_len)


ascii_table(32, 127, 10)


"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.
Решите через рекурсию. Решение через цикл не принимается.
"""


def chek(number, check_sum=0, check_expression=0):
    if check_sum == 0:
        check_expression = number * (number + 1) / 2

    check_sum += number
    if number == 1:
        return print(check_sum == check_expression)
    return chek(number-1, check_sum, check_expression)


chek(5)


# Переделка
# Отвлеклась от задания, пыталась сделать более универсально
def chek(number):
    if number == 1:
        return number
    return number + chek(number-1)


n = 5
print(chek(n) == (n * (n + 1) / 2))
# Или с вводом пользователя
try:
    n = int(input('Введите любое натуральное число: '))
    print(f'1+2+...+n == (n * (n + 1) / 2) for n={n} is', chek(n) == (n * (n + 1) / 2))
except ValueError:
    print('Вы ввели не натуральное число')