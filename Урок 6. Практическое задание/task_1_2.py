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
from pympler import asizeof


# Реализовать классы работника и на его базе класс его позиции в компании
# class Worker:
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         wage_dict = {"директор": 150000, "бухгалтер": 70000, "рабочий": 50000}
#         bonus_dict = {"директор": wage_dict[position]*1.5,
#                       "бухгалтер": wage_dict[position]*1.2,
#                       "рабочий": wage_dict[position]*1}
#         income_dict = {"wage": wage_dict[position], "bonus": bonus_dict[position]}
#         self._income = income_dict["wage"] + income_dict["bonus"]
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position):
#         super().__init__(name, surname, position)
#
#     def get_full_name(self):
#         print(f'{self.position.capitalize()}: {self.name} {self.surname}')
#
#     def get_total_income(self):
#         print(f'Доход с учетом премии: {self._income}')
#
#
# director = Position('Максим', 'Андреев', 'директор')
# director.get_full_name()
# director.get_total_income()
# print(asizeof.asizeof(director))    # -> 680
# print()
#
# accountant = Position('Сергей', 'Лызнов', 'бухгалтер')
# accountant.get_full_name()
# accountant.get_total_income()
# print(asizeof.asizeof(accountant))  # -> 680
# print()
#
# worker = Position('Тимофей', 'Халёнов', 'рабочий')
# worker.get_full_name()
# worker.get_total_income()
# print(asizeof.asizeof(worker))  # -> 680
# print()


# Используем слоты
class Worker:
    __slots__ = ['name', 'surname', 'position', '_income']

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        wage_dict = {"директор": 150000, "бухгалтер": 70000, "рабочий": 50000}
        bonus_dict = {"директор": wage_dict[position]*1.5,
                      "бухгалтер": wage_dict[position]*1.2,
                      "рабочий": wage_dict[position]*1}
        income_dict = {"wage": wage_dict[position], "bonus": bonus_dict[position]}
        self._income = income_dict["wage"] + income_dict["bonus"]


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'{self.position.capitalize()}: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income}')


director = Position('Максим', 'Андреев', 'директор')
director.get_full_name()
director.get_total_income()
print(asizeof.asizeof(director))    # -> 480
print()

accountant = Position('Сергей', 'Лызнов', 'бухгалтер')
accountant.get_full_name()
accountant.get_total_income()
print(asizeof.asizeof(accountant))  # -> 480
print()

worker = Position('Тимофей', 'Халёнов', 'рабочий')
worker.get_full_name()
worker.get_total_income()
print(asizeof.asizeof(accountant))  # -> 480
print()
