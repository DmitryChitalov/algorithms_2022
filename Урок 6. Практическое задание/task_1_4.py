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

Это файл для четвертого скрипта
"""

"""
Этот кусок кода - из ДЗ №5, в оригинале, преобразую его в функцию,
которая позволит работать с БОЛЬШИМ количеством данных
company_number = input('Введите количество организаций: ')
company_dict = defaultdict(str)
temp_tuple = namedtuple('company', 'company_name company_money_int company_avr company_money_year')
for n in range(int(company_number)):
    company_name = input('Введите имя компании: ')
    # Запрашиваем строку из поквартальных прибылей
    company_money = input('Через пробел введите прибыль данного предприятия '
                          'за каждый квартал(Всего 4 квартала): ')
    # Преобразовываем строку в список с типом элемента float (хотя к денежкам лучше применять decimal)
    company_money_int = [float(el) for el in company_money.split(' ')]
    # Вычисляем среднемесячную прибыль компании
    company_avr = mean(company_money_int)
    # Вычисляем годовую прибыль компании
    company_money_year = sum(company_money_int)
    # Формируем именнованый кортеж с полученными значениями
    temp_1 = temp_tuple(
        company_name=company_name, company_money_int=company_money_int,
        company_avr=company_avr, company_money_year=company_money_year)
    # Сохраняем в дефульто-словарь, где ключ - имя компании
    company_dict[company_name] = temp_1
# опционально проверяем получившийся словарь:
print(company_dict)
# Расчет среднегодовой прибыли:
money_year = float()
money_year = mean([company_dict[key].company_money_year for key in company_dict])
print(f'Среднегодовая прибыль компаний составит  - {money_year}')
# Оценка прибыльности компаний:
company_max = []
company_min = []
for key in company_dict:
    if company_dict[key].company_money_year >= money_year:
        company_max.append(company_dict[key].company_name)
    else:
        company_min.append(company_dict[key].company_name)
print(f'Предприятия, с прибылью выше среднего значения: {company_max}')
print(f'Предприятия, с прибылью ниже среднего значения: {company_min}')
"""
from random import randint
from collections import defaultdict, namedtuple
from statistics import mean
from memory_profiler import memory_usage
from time import perf_counter


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start = perf_counter()
        res = func(*args, **kwargs)
        stop = perf_counter()
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        print(f'Функция {func.__name__}, выполнение заняло: {mem_dif} Mib, время выполнения: {stop - start}')
        return res

    return wrapper


# company_1 - подготовленная неоптимизированная версия без использования ручного ввода
@memory
def company_1(company_number=1000):
    # company_number = input('Введите количество организаций: ') - по умолчанию ставим 1000
    name_gen = name_gen_1()
    company_dict = defaultdict(str)
    temp_tuple = namedtuple('company', 'company_name company_money_int company_avr company_money_year')
    for n in range(int(company_number)):
        # company_name = input('Введите имя компании: ') меняем ручной ввод на "генератор имен компаний"
        company_name = next(name_gen)
        # company_money = input('Через пробел введите прибыль данного предприятия '
        #                       'за каждый квартал(Всего 4 квартала): ')    генерируем прибыль рандомно
        company_money_int = [randint(100, 1000) for i in range(4)]
        # Вычисляем среднемесячную прибыль компании
        company_avr = mean(company_money_int)
        # Вычисляем годовую прибыль компании
        company_money_year = sum(company_money_int)
        # Формируем именнованый кортеж с полученными значениями
        temp_1 = temp_tuple(
            company_name=company_name, company_money_int=company_money_int,
            company_avr=company_avr, company_money_year=company_money_year)
        # Сохраняем в дефульто-словарь, где ключ - имя компании
        company_dict[company_name] = temp_1
    # опционально проверяем получившийся словарь:
    # print(company_dict)
    # Расчет среднегодовой прибыли:
    money_year = float()
    money_year = mean([company_dict[key].company_money_year for key in company_dict])
    print(f'Среднегодовая прибыль компаний составит  - {money_year}')
    # Оценка прибыльности компаний:
    company_max = []
    company_min = []
    for key in company_dict:
        if company_dict[key].company_money_year >= money_year:
            company_max.append(company_dict[key].company_name)
        else:
            company_min.append(company_dict[key].company_name)
    # print(f'Предприятия, с прибылью выше среднего значения: {company_max}')
    # print(f'Предприятия, с прибылью ниже среднего значения: {company_min}')


def name_gen_1():
    for el in range(1000):
        yield f'{el + 1}'


# Пробуем потимизировать: убираю del временные объекты:
@memory
def company_2(company_number=1000):
    # company_number = input('Введите количество организаций: ') - по умолчанию ставим 1000
    name_gen = name_gen_1()
    company_dict = defaultdict(str)
    temp_tuple = namedtuple('company', 'company_name company_money_int company_avr company_money_year')
    for n in range(int(company_number)):
        # company_name = input('Введите имя компании: ') меняем ручной ввод на "генератор имен компаний"
        company_name = next(name_gen)
        # company_money = input('Через пробел введите прибыль данного предприятия '
        #                       'за каждый квартал(Всего 4 квартала): ')    генерируем прибыль рандомно
        company_money_int = [randint(100, 1000) for i in range(4)]
        # Вычисляем среднемесячную прибыль компании
        company_avr = mean(company_money_int)
        # Вычисляем годовую прибыль компании
        company_money_year = sum(company_money_int)
        # Формируем именнованый кортеж с полученными значениями
        temp_1 = temp_tuple(
            company_name=company_name, company_money_int=company_money_int,
            company_avr=company_avr, company_money_year=company_money_year)
        # Сохраняем в дефульто-словарь, где ключ - имя компании
        company_dict[company_name] = temp_1
        del temp_1
    # опционально проверяем получившийся словарь:
    # print(company_dict)
    # Расчет среднегодовой прибыли:
    money_year = float()
    money_year = mean([company_dict[key].company_money_year for key in company_dict])
    print(f'Среднегодовая прибыль компаний составит  - {money_year}')
    # Оценка прибыльности компаний:
    company_max = []
    company_min = []
    for key in company_dict:
        if company_dict[key].company_money_year >= money_year:
            company_max.append(company_dict[key].company_name)
        else:
            company_min.append(company_dict[key].company_name)
    # print(f'Предприятия, с прибылью выше среднего значения: {company_max}')
    # print(f'Предприятия, с прибылью ниже среднего значения: {company_min}')


company_1()
company_2()

"""
Мои результаты замеров :
Среднегодовая прибыль компаний составит  - 2213.64
Функция company_1, выполнение заняло: 0.45703125 Mib, время выполнения: 0.017498299945145845
Среднегодовая прибыль компаний составит  - 2199.381
Функция company_2, выполнение заняло: 0.03515625 Mib, время выполнения: 0.01971440005581826
(вывод строки о среднегодовой прибыли оставил специально, что бы ориентироваться на корректность работы кода)
И снова использование всего одной строки кода дает очень наглядный результат по оптимизации использования памяти.
Нужно не забывать удалять временный объекты и дальше.
"""
