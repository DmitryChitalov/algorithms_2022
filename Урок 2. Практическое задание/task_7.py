"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5 #15
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""

def checker(input_number, result=0, left_side=0):
      
    if result == input_number:
        right_side = input_number * (input_number + 1) / 2  
        if left_side == right_side:
            return print(True)
        else:
            return print(False)        

    result += 1   
    left_side += result    
    return checker(input_number, result, left_side)


checker(5)
checker(17)
checker(86)
