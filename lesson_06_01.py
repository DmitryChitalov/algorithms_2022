from pympler import asizeof
# Курс основ, 9 урок
# Использовала __slots__ для хранения атрибутов и значений в кортеже, вместо словаря. Это сократило размер объекта
# c 960 на 640


class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': _income, 'bonus': int(_income * 0.2)}


class Position(Worker):
    def get_full_name(self):
        return print(f'Full name: {self.surname} {self.name}')

    def get_total_income(self):
        total_income = self._income['salary'] + self._income['bonus']
        return print(f'Total income for {self.position} is {total_income}')


position_obj = Worker('Ivan', 'Ivanov', 'manager', 1000)
print(asizeof.asizeof(position_obj))  # --> 960


class Worker_2:
    __slots__ = ('name', 'surname', 'position', '_income')

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': _income, 'bonus': int(_income * 0.2)}

    @property
    def income(self):
        return self._income


class Position_2(Worker):
    def get_full_name(self):
        return print(f'Full name: {self.surname} {self.name}')

    def get_total_income(self):
        total_income = self._income['salary'] + self._income['bonus']
        return print(f'Total income for {self.position} is {total_income}')


position_2_obj = Worker_2('Ivan', 'Ivanov', 'manager', 1000)
print(asizeof.asizeof(position_2_obj))  # --> 640

