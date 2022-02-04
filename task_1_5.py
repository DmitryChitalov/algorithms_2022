# Задание с курса по основам

from pympler import asizeof


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(f'Сотрудник - {full_name}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'ЗП с учетом премии {total_income}')


staff_1 = Position('Kale', 'Williams', 'manager', 3000, '2000')
print(asizeof.asizeof(staff_1))


class Worker2:
    __slots__ = ['name', 'surname', 'position', 'wage', '_income']

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


# Для оптимизации - использование слотов. Размер объекта без слотов - 552, со слотами - 440.


class Position(Worker2):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(f'Сотрудник - {full_name}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'ЗП с учетом премии {total_income}')


staff_2_1 = Position('Kale', 'Williams', 'manager', 3000, '2000')
print(asizeof.asizeof(staff_2_1))
