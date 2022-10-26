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

Это файл для третьего скрипта
"""
"""
Основы Python урок 6.
2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

from memory_profiler import profile


# Первый вариант получения IP-адреса практически не удалось оптимизировать, у него более длинный код, но он написан на
# основе словаря и даже удаление созданного словаря не даёт существенного уменьшения используемой памяти.
# Изменения показаны в комментариях кода.
@profile
def get_spam_addr():
    """Находит адрес пославший больше всего запросов и возвращает кортеж (адрес, число запросов)"""
    dict_remote_addr = {}
    with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
        for str_ in fr:
            if not str_.split()[0] in dict_remote_addr:
                dict_remote_addr.setdefault(str_.split()[0], 1)  # Создаём позицию IP адрес: запрос в dict_remote_addr
            else:
                dict_remote_addr[str_.split()[0]] += 1

    max_count_addr = 0
    spam_addr = ''
    for key, val in dict_remote_addr.items():
        if val > max_count_addr:
            spam_addr = key
            max_count_addr = val
    del dict_remote_addr  # Удаление словаря после его использования.
    return print('IP aдрес спамера и число его запросов: ', spam_addr, max_count_addr)  # вернёт кортеж значений
    # (адрес, число запросов)


# Во втором варианте удалось существенно снизить используемую память за счёт профилллирования.
# Снижение памяти удалось достичь, убрав из программы нецелесообразный список.
# Выигрыш в памяти почти 50%!!!
@profile
def get_spam_adrr_1():
    with open('nginx_logs.txt') as f:
        # data = []  # Убираем ненужный список.
        spam_dict = {}
        for line in f:
            splitted = line.split()
            # data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))  # Убираем ненужный список.
            spam_dict.setdefault(splitted[0], 0)
            spam_dict[splitted[0]] += 1

    spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
    spamer = spam_dict[:1]
    del spam_dict
    print(spamer)  # Not only one spamer


get_spam_addr()
get_spam_adrr_1()

"""
Приведу профили замеров памяти до и после изменений. Оба варианта решений рабочии. Файл логов сервера nginx_logs.txt
прилагаю. Вывод при парсинге логов предпочтительнее использовать словари!

ДО:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    45     19.3 MiB     19.3 MiB           1   @profile
    46                                         def get_spam_addr():
    47                                             '''Находит адрес пославший больше всего запросов и возвращает 
                                                     кортеж (адрес, число запросов)'''
    48     19.3 MiB      0.0 MiB           1       dict_remote_addr = {}
    49     19.6 MiB      0.0 MiB           2       with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    50     19.6 MiB      0.0 MiB       51463           for str_ in fr:
    51     19.6 MiB      0.1 MiB       51462               if not str_.split()[0] in dict_remote_addr:
    52     19.6 MiB      0.1 MiB        2660                   dict_remote_addr.setdefault(str_.split()[0], 1)  
                                                             # Создаём позицию IP адрес: запрос в dict_remote_addr
    53                                                     else:
    54     19.6 MiB      0.0 MiB       48802                   dict_remote_addr[str_.split()[0]] += 1
    55                                         
    56     19.6 MiB      0.0 MiB           1       max_count_addr = 0
    57     19.6 MiB      0.0 MiB           1       spam_addr = ''
    58     19.6 MiB      0.0 MiB        2661       for key, val in dict_remote_addr.items():
    59     19.6 MiB      0.0 MiB        2660           if val > max_count_addr:
    60     19.6 MiB      0.0 MiB           4               spam_addr = key
    61     19.6 MiB      0.0 MiB           4               max_count_addr = val
    62                                             #del dict_remote_addr  # Удаление словаря после его использования.
    63     19.6 MiB      0.0 MiB           1       return print('IP aдрес спамера и число его запросов: ', 
                                                    spam_addr, max_count_addr)  # вернёт кортеж значений
    64                                                        # (адрес, число запросов)

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    69     19.6 MiB     19.6 MiB           1   @profile
    70                                         def get_spam_adrr_1():
    71     34.5 MiB      0.0 MiB           2       with open('nginx_logs.txt') as f:
    72     19.6 MiB      0.0 MiB           1           data = []  # Убираем ненужный список.
    73     19.6 MiB      0.0 MiB           1           spam_dict = {}
    74     34.5 MiB      0.0 MiB       51463           for line in f:
    75     34.5 MiB     13.3 MiB       51462               splitted = line.split()
    76     34.5 MiB      1.6 MiB       51462               data.append((splitted[0], splitted[5].replace('"', ''), 
                                                                    splitted[6]))  # Убираем ненужный список.
    77     34.5 MiB      0.0 MiB       51462               spam_dict.setdefault(splitted[0], 0)
    78     34.5 MiB      0.0 MiB       51462               spam_dict[splitted[0]] += 1
    79                                         
    80                                         
    81     34.6 MiB      0.1 MiB        5321       spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
    82     34.6 MiB      0.0 MiB           1       spamer = spam_dict[:1]
    83                                             #del spam_dict
    84     34.6 MiB      0.0 MiB           1       print(spamer)  # Not only one spamer

ПОСЛЕ:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    45     19.4 MiB     19.4 MiB           1   @profile
    46                                         def get_spam_addr():
    47                                             
    48     19.4 MiB      0.0 MiB           1       dict_remote_addr = {}
    49     19.7 MiB      0.0 MiB           2       with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    50     19.7 MiB      0.0 MiB       51463           for str_ in fr:
    51     19.7 MiB      0.1 MiB       51462               if not str_.split()[0] in dict_remote_addr:
    52     19.7 MiB      0.1 MiB        2660                   dict_remote_addr.setdefault(str_.split()[0], 1)  
    53                                                     else:
    54     19.7 MiB      0.0 MiB       48802                   dict_remote_addr[str_.split()[0]] += 1
    55                                         
    56     19.7 MiB      0.0 MiB           1       max_count_addr = 0
    57     19.7 MiB      0.0 MiB           1       spam_addr = ''
    58     19.7 MiB      0.0 MiB        2661       for key, val in dict_remote_addr.items():
    59     19.7 MiB      0.0 MiB        2660           if val > max_count_addr:
    60     19.7 MiB      0.0 MiB           4               spam_addr = key
    61     19.7 MiB      0.0 MiB           4               max_count_addr = val
    62     19.7 MiB      0.0 MiB           1       del dict_remote_addr  # Удаление словаря после его использования.
    63     19.7 MiB      0.0 MiB           1       return print('IP aдрес спамера и число его запросов: ', 
                                                    spam_addr, max_count_addr)  # вернёт кортеж значений
    64                                             # (адрес, число запросов)

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    69     19.7 MiB     19.7 MiB           1   @profile
    70                                         def get_spam_adrr_1():
    71     19.7 MiB      0.0 MiB           2       with open('nginx_logs.txt') as f:
    72                                                 #data = []  # Убираем ненужный список.
    73     19.7 MiB      0.0 MiB           1           spam_dict = {}
    74     19.7 MiB      0.0 MiB       51463           for line in f:
    75     19.7 MiB      0.0 MiB       51462               splitted = line.split()
    76                                                     #data.append((splitted[0], splitted[5].replace('"', ''), 
                                                                splitted[6]))  # Убираем ненужный список.
    77     19.7 MiB      0.0 MiB       51462               spam_dict.setdefault(splitted[0], 0)
    78     19.7 MiB      0.0 MiB       51462               spam_dict[splitted[0]] += 1
    79                                         
    80                                         
    81     19.9 MiB      0.1 MiB        5321       spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
    82     19.9 MiB      0.0 MiB           1       spamer = spam_dict[:1]
    83     19.9 MiB      0.0 MiB           1       del spam_dict
    84     19.9 MiB      0.0 MiB           1       print(spamer)  # Not only one spamer

"""
