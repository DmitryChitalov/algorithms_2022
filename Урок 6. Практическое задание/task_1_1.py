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
'''
Урок 5 задание 1. курс алгоритмы и структуры данных
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
'''
from memory_profiler import profile
from collections import namedtuple
from collections import OrderedDict
import sys

amaunt = int(input('введите кол-во предприятий '))
enterprise = namedtuple('enterprise', ['Name', 'q1', 'q2', 'q3', 'q4'])
full_dict = OrderedDict()
middle = 0


def one_enterprise():
    name = input('введите название предприятия ')
    p_li = []
    for i in range(4):
        pr = input(f'введите прибыль за {i+1} квартал ')
        p_li.append(float(pr))
    ent = enterprise(name, q1=p_li[0], q2=p_li[1], q3=p_li[2], q4=p_li[3])
    full_dict[name] = ent


def calculate_middle_profit():
    for _ in range(amaunt):
        one_enterprise()
    sum_one = []
    for k, v in full_dict.items():
        sum_one.append(v.q1+v.q2+v.q3+v.q4)
    global middle
    middle = sum(sum_one)/len(sum_one)
    print(f'Средняя годовая прибыль всех предприятий: {middle}')

@profile
def main_downstream_or_upstream():
    calculate_middle_profit()
    up = 'Cумма прибыли больше среднего у: '
    down = 'Cумма прибыли меньше среднего у: '
    global middle
    for k, v in full_dict.items():
        sum_one = v.q1+v.q2+v.q3+v.q4
        if sum_one > middle:
            up += k + ' '
        else:
            down += k + ' '


    print(f'использовано памяти {sys.getsizeof(full_dict)}')
    print(up)
    print(down)


main_downstream_or_upstream()
'''Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    88     17.5 MiB     17.5 MiB           1   @profile
    89                                         def main_downstream_or_upstream():
    90     17.5 MiB      0.0 MiB           1       calculate_middle_profit()
    91     17.5 MiB      0.0 MiB           1       up = 'Cумма прибыли больше среднего у: '
    92     17.5 MiB      0.0 MiB           1       down = 'Cумма прибыли меньше среднего у: '
    93                                             global middle
    94     17.5 MiB      0.0 MiB           3       for k, v in full_dict.items():
    95     17.5 MiB      0.0 MiB           2           sum_one = v.q1+v.q2+v.q3+v.q4
    96     17.5 MiB      0.0 MiB           2           if sum_one > middle:
    97     17.5 MiB      0.0 MiB           1               up += k + ' '
    98                                                 else:
    99     17.5 MiB      0.0 MiB           1               down += k + ' '
   100     17.5 MiB      0.0 MiB           1       print(up)
   101     17.5 MiB      0.0 MiB           1       print(down)'''




from collections import deque
full_dict = OrderedDict()
middle = 0

class Enterprise():
    def __init__(self,name):
        self.name = name
        self.profobility = 0

    def get_prof(self):
        return self.profobility

    def set_prof(self,li):
        self.profobility = li

    def prof_one_enterp(self):
        return sum(self.profobility)/len(self.profobility)
    

class Main():
    def __init__(self):
        self.all_enterprises = []


    def get_enterprise(self):
        name = input('введите название предприятия ')
        ent = Enterprise(name)
        p_li = []
        for i in range(4):
            pr = input(f'введите прибыль за {i+1} квартал ')
            p_li.append(float(pr))
        print(f' li prof {p_li}')
        ent.set_prof(p_li)
        self.all_enterprises.append(ent)

    def run(self):
        count_ent = int(input('введите кол-во предприятий '))
        for _ in range(count_ent):
            self.get_enterprise()
        self.get_result()

    def calculate_middle_profit(self):
        sum_one = []
        for ent in self.all_enterprises:
            li_ent = ent.get_prof()
            sum_one.extend(li_ent)

        middle = sum(sum_one)/len(sum_one)
        print(f'Средняя годовая прибыль всех предприятий: {middle}')
        return middle

    def get_result(self):
        midl = self.calculate_middle_profit()
        for ent in self.all_enterprises:
            if ent.prof_one_enterp() < midl:
                print(f'Cумма прибыли меньше среднего у: {ent.name}')
            else:
                print(f'Cумма прибыли больше среднего у: {ent.name}')
 
    
m = Main()
m.run()
print(sys.getsizeof(m))




'''выводы произвел переработку задания на ООП при этом
использование памяти для списков без ооп 424
с ООП все классы занали 48'''