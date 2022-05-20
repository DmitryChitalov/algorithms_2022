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

def summ_numbers(number, answer=1, counter=0):

    number -= 1
    
    if number == 0:
        return answer
        
    else:
        num = answer
        
        if counter % 2 == 0:
            answer = float(answer) / -2

        else:
            answer = float(answer) / 2

        answer = num + answer
        counter += 1

        return summ_numbers(number=number, answer=answer, counter=counter)


if __name__ == '__main__':

    answer = int(input('Введите количество элементов: '))
    print('Количество элементов - {}, их сумма - {}'.format(answer, summ_numbers(number=answer)))
