from memory_profiler import memory_usage



'''
задание из  основ Python. Вернуть кортежи учеников и классов, если в списке классов
нет значений, то вернуть None. 
tutor_class, генератор, использует 0.0 mib, возвращает каждый раз новый элемент 
либо через цикл for либо через метод next()
tutor_class_2, списковое включение, использует 0.04296875 mib функция возвращает весь список целиком, поэтому она 
потребляет больше памяти чем генератор.
'''

tutors = [chr(i) for i in range(2000)]  #['Иван', 'Анастасия', 'Петр', 'Сергей', 'Александр']
klasses = [chr(i) for i in range(1000)]#['9А', '7В', '9Б']



def decor(func):
    def wrapper():
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper

@decor
def tutor_class():
    for i in range(len(tutors)):
     if i < len(klasses):
        yield tutors[i], klasses[i]
     else:
         yield tutors[i], None



@decor
def tutor_class_2():
    res = [(tutors[i], klasses[i]) if i < len(klasses) else
           (tutors[i], None) for i in range(len(tutors))]
    return res


print(f'tutor_class, генератор, использует {tutor_class()} mib')
print(f'tutor_class_2, списковое включение, использует {tutor_class_2()} mib')


'''
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.

0.125 рекурсия
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
def func(n, s=0):
    if n == 0:
        return s
    else:
        s += n
        return func(n-1, s)

@decor
def func_2(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


n = 100
print(func(n))
print(func_2(n))





