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

from pympler.asizeof import asizeof

# Курс Основы Python lesson_9 task_2

# До оптимизации


# class Worker:
#
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = dict(income)
#
#
# class Position(Worker):
#     def get_full_name(self):
#         print(f'Работник: {self.surname} {self.name} \n'
#               f'Должность: {self.position}')
#
#     def get_total_income(self):
#         total_income = self._income['wage'] + self._income['bonus']
#         print('Полный доход составляет: ', total_income)
#
#
# worker = Position('Иван', 'Иванов', 'механик', {'wage': 10000, 'bonus': 20000})
# print(f'Размер объекта до оптимизации: {asizeof(worker)}')


# После оптимизации

class Worker:
    __slots__ = 'name', 'surname', 'position', '_income'

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(income)


class Position(Worker):
    def get_full_name(self):
        print(f'Работник: {self.surname} {self.name} \n'
              f'Должность: {self.position}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print('Полный доход составляет: ', total_income)


worker = Position('Иван', 'Иванов', 'механик', {'wage': 10000, 'bonus': 20000})

print(f'Размер объекта после оптимизации: {asizeof(worker)}')

"""
В с помощью __slots__ экономлю память, расширять атрибуты класса не планирую,
поэтому имеет смысл задействовать этот метод

Размер объекта до оптимизации: 1056
Размер объекта после оптимизации: 856
"""
