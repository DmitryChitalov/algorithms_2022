from memory_profiler import memory_usage




'''
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
0.08203125 рекурсия
0.0 обычная функция
Рекурсивные функции занимают больше места в памяти по сравнению с итеративными 
из-за постоянного добавления новых слоев в стек в памяти, пока не дойдёт до базового случая
Это происходит благодаря процессу LIFO (last in, first out, «последним пришел — первым ушел»)
'''


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


@decor
def flip_over(num, res=''):
    if num == 0:
        return res
    else:
        x = num % 10
        num = num // 10
        res += str(x)
    return flip_over(num, res)



@decor
def flip_over_2(enter_num):
    return str(enter_num)[::-1]


num = 9132234523452345234523453742234523452345234523453

print(flip_over(num))
print(flip_over_2(num))


