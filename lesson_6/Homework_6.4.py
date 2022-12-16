from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:['инженер-конструктор Игорь',
# 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']. Вывести: "Привет, Имя!"
workers_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                           'аэлита',
                'инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                           'аэлита'
                'инженер-конструктор Игорь',
                'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                              'аэлита']


# @decor
# def hello_name_1(lst):
#     for i in range(len(lst)):
#         worker_name_letters_list = list(lst[i].split()[len(lst[i].split())-1])
#         name_str = ''
#         for j in range(len(worker_name_letters_list)):
#             if j == 0:
#                 worker_name_letters_list[j] = worker_name_letters_list[j].upper()
#                 name_str += worker_name_letters_list[j]
#             else:
#                 worker_name_letters_list[j] = worker_name_letters_list[j].lower()
#                 name_str += worker_name_letters_list[j]
#             if j == len(worker_name_letters_list)-1:
#                 print('Привет,', name_str+'!')
#
#
# _, mem1 = hello_name_1(workers_list)
# print(mem1)
# Выполнение заняло 0.0078125 Mib

# Используем кортеж, будем избавляться от ненужных переменных, сделаем f-строку
@decor
def hello_name_2(lst):
    tpl = tuple(lst)
    del lst
    for i in range(len(tpl)):
        name_str = ''
        worker_name_letters_tpl = tuple(tpl[i].split()[len(tpl[i].split()) - 1])
        for j in range(len(worker_name_letters_tpl)):
            name_str += str(worker_name_letters_tpl[j])
        print(f'Привет, {name_str.capitalize()}!')
        del name_str


_, mem2 = hello_name_2(workers_list)
print(mem2)
# Выполнение заняло 0.00390625 Mib