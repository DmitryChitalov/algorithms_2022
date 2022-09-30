"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""
'''
Урок 2 Задача 2
Для оптимизации использования памяти была произведена замена рекурсии, при работе которой используется стек вызовов
на цикл for. Замеры подтвердили оптимизацию использования памяти.
'''

even_numbers = []
odd_numbers = []
my_number = 14785236987456125896321147622545633121455222145563322114552333552126363366522222


@profile
def func():
    def number_parsing(number):
        if number == 0:
            return len(even_numbers), len(odd_numbers)
        else:
            if number // 10 >= 0 and number % 2 != 0:
                odd_numbers.append(1)
                number = number // 10
            else:
                even_numbers.append(1)
                number = number // 10
            return number_parsing(number)

    print(f'Количество четных и нечетных цифр в числе равно: {number_parsing(my_number)}')
    
    
func()

""" 
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    53     13.8 MiB     13.8 MiB           1   @profile
    54                                         def func():
    55     13.9 MiB      0.0 MiB          82       def number_parsing(number):
    56     13.9 MiB      0.0 MiB          81           if number == 0:
    57     13.9 MiB      0.0 MiB           1               return len(even_numbers), len(odd_numbers)
    58                                                 else:
    59     13.8 MiB      0.0 MiB          80               if number // 10 >= 0 and number % 2 != 0:
    60     13.8 MiB      0.0 MiB          41                   odd_numbers.append(1)
    61     13.8 MiB      0.0 MiB          41                   number = number // 10
    62                                                     else:
    63     13.8 MiB      0.0 MiB          39                   even_numbers.append(1)
    64     13.8 MiB      0.0 MiB          39                   number = number // 10
    65     13.9 MiB      0.0 MiB          80               return number_parsing(number)
    66                                         
    67     13.9 MiB      0.0 MiB           1       print(f'Количество четных и нечетных цифр в числе равно: {number_parsing(my_number)}')



Process finished with exit code 0
"""


@profile
def number_parsing_for(number):
    for i in str(number):
        if int(i) % 2 != 0:
            odd_numbers.append(1)
        else:
            even_numbers.append(1)
    return len(even_numbers), len(odd_numbers)


"""
print(f'Количество четных и нечетных цифр в числе равно: {number_parsing_for(my_number)}')
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    97     13.8 MiB     13.8 MiB           1   @profile
    98                                         def number_parsing_for(number):
    99     13.8 MiB      0.0 MiB          81       for i in str(number):
   100     13.8 MiB      0.0 MiB          80           if int(i) % 2 != 0:
   101     13.8 MiB      0.0 MiB          41               odd_numbers.append(1)
   102                                                 else:
   103     13.8 MiB      0.0 MiB          39               even_numbers.append(1)
   104     13.8 MiB      0.0 MiB           1       return len(even_numbers), len(odd_numbers)


Количество четных и нечетных цифр в числе равно: (39, 41)

Process finished with exit code 0
"""