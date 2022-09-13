"""
КУРС: "Основы языка Python". Урок 9: "ООП". Задание 3.
Реализовать базовый класс `Worker` (работник):
* определить атрибуты: `name`, `surname`, `position` (должность), `income` (доход);
* последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
  например, `{"wage": wage, "bonus": bonus}`;
* создать класс `Position` (должность) на базе класса `Worker`;
* в классе `Position` реализовать методы получения полного имени сотрудника (`get_full_name`) и дохода с
  учётом премии (`get_total_income`);
* проверить работу примера на реальных данных: создать экземпляры класса `Position`, передать данные,
  проверить значения атрибутов, вызвать методы экземпляров.
"""
from pympler.asizeof import asizeof


# https://github.com/AzarnykhOleg/Python-Basics/pull/10
class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name: str = name
        self.surname: str = surname
        self.position: str = position
        self._income: dict = income


class Position(Worker):
    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f'{self.name} {self.surname}'.title()

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        return sum(self._income.values())


welder = Position('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})


# Обновлённый вариант:
class WorkerOne:
    __slots__ = 'name', 'surname', 'position', '_income'

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name: str = name
        self.surname: str = surname
        self.position: str = position
        self._income: dict = income


class PositionOne(WorkerOne):
    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f'{self.name} {self.surname}'.title()

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        return sum(self._income.values())


welder_1 = PositionOne('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})

if __name__ == '__main__':
    print(welder.get_full_name(), welder.get_total_income())
    print(asizeof(welder))  # -> 1088
    print('----------------- Новый вариант -----------------')
    print(welder_1.get_full_name(), welder_1.get_total_income())
    print(asizeof(welder_1))  # -> 888

"""
Задействование атрибута __slots__ при создании Класса позволило явно объявить элементы данных (свойства) 
и запретить создание словаря __dict__. Экономия пространства от запрета использования __dict__, 
в нашем случае составила 18,4 % (888 vs 1088) на 1 экзмпляре класса.
Скорость поиска атрибутов так же увеличена.
"""