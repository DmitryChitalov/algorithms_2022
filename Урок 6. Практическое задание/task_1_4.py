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
Python-basic - https://github.com/Frvzr/gb_python_basics/tree/master/Koposhilov_Ivan_dz_9
Реализовать базовый класс Worker (работник):

определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

# Исходный вариант




from pympler import asizeof
class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position(Worker):
    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        self.full_name = f'{self.name.title()} {self.surname.title()}'
        return self.full_name

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        self.result = f'{sum(self.income.values())}'
        return self.result


if __name__ == '__main__':
    welder = Position('иван', 'васильев', 'сварщик', {
                      'wage': 50000, 'bonus': 15000})
    driver = Position('петр', 'николаев', 'водитель',
                      {'wage': 30000, 'bonus': 7500})
    scientist = Position('геннадий', 'разумов', 'ученый',
                         {'wage': 150000, 'bonus': 25000})
    # Иван Васильев 65000
    print(welder.get_full_name(), welder.get_total_income())
    # Петр Николаев 37500
    print(driver.get_full_name(), driver.get_total_income())
    # Геннадий Разумов 175000
    print(scientist.get_full_name(), scientist.get_total_income())
    print(asizeof.asizeof(welder))

# Оптимизированный через __slots__


class WorkerNewr:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class PositionNew(Worker):
    __slots__ = ('name', 'surname', 'position', 'income', 'result')

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        self.full_name = f'{self.name.title()} {self.surname.title()}'
        return self.full_name

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        self.result = f'{sum(self.income.values())}'
        return self.result


if __name__ == '__main__':
    welder = PositionNew('иван', 'васильев', 'сварщик', {
        'wage': 50000, 'bonus': 15000})
    driver = PositionNew('петр', 'николаев', 'водитель',
                         {'wage': 30000, 'bonus': 7500})
    scientist = PositionNew('геннадий', 'разумов', 'ученый',
                            {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(), welder.get_total_income())
    print(driver.get_full_name(), driver.get_total_income())
    print(scientist.get_full_name(), scientist.get_total_income())
    print(asizeof.asizeof(welder))

"""
Добавление слотов в наследованный класс, снизило потребление памяти
1-й вариант = 1600
2-ой вариант = 1096
"""
