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
from memory_profiler import profile

"""---------------------------------------
1.2 Для ОПТИМИЗАЦИИ используем СЛОТЫ в ООП 
------------------------------------------"""


# Курс 'Основы PYTHON'
# 9.3. Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# немного упростил реализацию для класса (в одном классе) для сравнения с оптимизированным
class Worker:
    workers = []

    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}
        Worker.workers.append(self)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]

    def __str__(self):
        return f'{self.get_full_name()} /{self.position}/ income: {self.get_total_income()}'


class Employee:
    __slots__ = ['name', 'surname', 'position', 'income', 'wage', 'bonus']
    employees = []

    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        Employee.employees.append(self)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.wage + self.bonus

    def __str__(self):
        return f'{self.get_full_name()} /{self.position}/ income: {self.get_total_income()}'


# Проверяем, что функционал одинаковый
pos_1, pos_2 = Worker('Bob', 'Lee', 'waiter', 3000, 500), Worker('Anna', 'Fio', 'chef', 6000, 4000)
print(f'{Worker.workers[0]}\n{Worker.workers[1]}')
p_1, p_2 = Employee('Bob', 'Lee', 'waiter', 3000, 500), Employee('Anna', 'Fio', 'chef', 6000, 4000)
print(f'{Employee.employees[0]}\n{Employee.employees[1]}')


@profile
def old_class():
    for val in data:
        Worker(*val)
    return len(Worker.workers)


@profile
def opt_class():
    for val in data:
        Employee(*val)
    return len(Employee.employees)


number = 100000
data = [(f'Name{i}', f'LastN{i}', f'Position{i}', i * 100, i * 10) for i in range(number)]
print(old_class())
print(opt_class())

"""
Результаты тестов показали, что новый класс Employee заметно оптимизирован по памяти с помощью использования
конструкции __slots__ при определении класса, который заменяет затратные по памяти словари для хранения атрибутов
на менее затратные по памяти контейнеры – списки, кортежи.

Line  Mem usage  Increment   Occur   Line Contents        | Line  Mem usage  Increment   Occur   Line Contents   
===================================================       | ===================================================
  93   54.2 MiB   54.2 MiB       1   @profile             |  100   93.6 MiB   93.6 MiB       1   @profile
  94                                 def old_class():     |  101                                 def opt_class():
  95   93.5 MiB    0.0 MiB  100001       for val in data: |  102  102.1 MiB    0.0 MiB  100001       for val in data:
  96   93.5 MiB   39.3 MiB  100000           Worker(*val) |  103  102.1 MiB    8.6 MiB  100000           Employee(*val)
  97   93.6 MiB    0.0 MiB       1       return len       |  104  102.1 MiB    0.0 MiB       1       return len
"""
