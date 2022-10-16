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

Это файл для первого скрипта

"""
# Python_intro_ 6_1
# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Техническое задание
#
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: '(<remote_addr>, <request_type>, <requested_resource>)'. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Формат вывода результата:
#
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]
# Аналитика:
#
#  C генератором счетчик памяти @profile  не работает,
#  proof:   https://github.com/pythonprofilers/memory_profiler/issues/42
#
# вариант parser1() выводит реззультат как  список IP адресов в формате list
# Выполнение заняло 17.4453125 Mib
#
# вариант parser2() выполнен как генератор, выдает строки по требованию,
# Использует память:
# Выполнение заняло 0.0 Mib
#
# В варианте с parser2() , который выполнен как генератор,  памяти требуется меньше
#
# Script listing:
# Выполнение заняло 17.4453125 Mib
# Выполнение заняло 0.0 Mib
#
# Process finished with exit code 0


from memory_profiler import profile
from memory_profiler import memory_usage
from urllib import request

url_addr = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res
    return wrapper


# @profile
@memory
def parser1():
    result_lst = []
    with request.urlopen(url_addr) as content:
        while True:
            string1 = str(content.readline().decode('utf-8'))
            if string1 == "":
                break
            string1a = string1[:string1.find('-')-1]    # 93.180.71.3
            # print(f'string 1 = {string1}')
            # print(f'string 1a = {string1a}')

            string2 = string1.split('"')[1]             # GET /downloads/product_1 HTTP/1.1
            string2a = string2.split('/')[0][:-1]       # GET
            string2b = string2.split(' ')[1][1:]        # downloads/product_1

            result_tup = (string1a, string2a, string2b)
            # print(f'result TUP =  {result_tup}')
            # print(result_tup)                          # used for debugging
            result_lst.append(result_tup)
            # print(result_lst)
    return result_lst


@memory
# @profile
def parser2():
    with request.urlopen(url_addr) as content:
        while True:
            string21 = str(content.readline().decode('utf-8'))
            if string21 == "":
                return
            string21a = string21[:string21.find('-')-1]     # 93.180.71.3
            string22 = string21.split('"')[1]               # GET /downloads/product_1 HTTP/1.1
            string22a = string22.split('/')[0][:-1]         # GET
            string22b = string22.split(' ')[1][1:]          # downloads/product_1
            result_tup = (string21a, string22a, string22b)
            yield result_tup
            continue


res_list = parser1()
#for string in res_list:
#    print(string)

gen1 = parser2()
while True:
    try:
        gen_line = next(gen1)
        # print(gen_line)
    except StopIteration:
        break
#
# Script listing:
# Выполнение заняло 17.4453125 Mib
# Выполнение заняло 0.0 Mib
#
# Process finished with exit code 0


