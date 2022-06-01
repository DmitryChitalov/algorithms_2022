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

# Скрипт взят из курса основы Python, ДЗ-9, task_3.

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
Для оптимизации используем новый класс Employee. Оптимизация происходит за счёт использования
конструкции __slots__.

"""