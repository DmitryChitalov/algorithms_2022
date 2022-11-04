"""
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

"""
"""
Это задание из курса основ второй урок
Пришлось список из задачи заменить на символы, чтобы увидеть разницу в используемой памяти.
Заменил список на генератор и убрал лишние списки


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     20.1 MiB     20.1 MiB           1   @profile()
    13                                         def convert_name_extract(list_in: list) -> list:
    14                                             
    15     20.1 MiB      0.0 MiB           1       list_out = []
    16     20.1 MiB      0.0 MiB           1       i = 0
    17     21.0 MiB      0.0 MiB       10026       for text in list_in:
    18     21.0 MiB      0.0 MiB       10025           text1 = text
    19                                                 # print(text1)
    20     21.0 MiB      0.0 MiB       10025           parts = text1.split(' ')
    21                                                 # print(parts)
    22     21.0 MiB      0.8 MiB       10025           text2 = (parts.pop()).capitalize()
    23                                                 # print(text2)
    24     21.0 MiB      0.1 MiB       10025           list_out.append(text2)
    25                                             # print(list_out)
    26     21.2 MiB      0.0 MiB       10026       for name in list_out:
    27     21.2 MiB      0.2 MiB       10025           greeting = f'Привет, {name}!'
    28                                                 # print(greeting)
    29     21.2 MiB      0.0 MiB       10025           list_out[i] = greeting
    30     21.2 MiB      0.0 MiB       10025           i += 1
    31                                             # return list_out


None
<generator object convert_name_extract_upd.<locals>.<genexpr> at 0x00000168A0A83B30>
Filename: C:\python_projects\Algoritm\lesson_6\task_1\task_1_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    38     20.5 MiB     20.5 MiB           1   @profile()
    39                                         def convert_name_extract_upd(list_in: list) -> list:
    40                                             
    41     20.5 MiB      0.0 MiB       20053       gen_out = (el.split(' ').pop().capitalize() for el in list_in)
    42     20.5 MiB      0.0 MiB           1       print(gen_out)
    43     20.5 MiB      0.0 MiB       10026       for name in gen_out:
    44                                                 # print(f'Привет, {name}!')
    45     20.5 MiB      0.0 MiB       10025           a = name
    46     20.5 MiB      0.0 MiB           1       return 1

"""

from memory_profiler import profile


@profile()
def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    i = 0
    for text in list_in:
        text1 = text
    
        parts = text1.split(' ')
    
        text2 = (parts.pop()).capitalize()
    
        list_out.append(text2)
    
    for name in list_out:
        greeting = f'Привет, {name}!'
        
        list_out[i] = greeting
        i += 1
    return list_out


my_list = [chr(code) for code in range(ord('a'), ord('z') + 10000)]
result = convert_name_extract(my_list)
print(result)

@profile()
def convert_name_extract_upd(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    gen_out = (el.split(' ').pop().capitalize() for el in list_in)
    
    for name in gen_out:
        print(f'Привет, {name}!')
        
    return 1

print(convert_name_extract_upd(my_list))
