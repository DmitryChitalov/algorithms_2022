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
# Основы. Урок 9. Задание 3
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.
from pympler.asizeof import asizeof
from collections import namedtuple


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int and float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return round(self._income['wage'] + self._income['wage'] * self._income['bonus'], 2)


class Worker_2:
    __slots__ = ['name', 'surname', 'position', 'wage', 'bonus', '_income']
    __pattern_income = namedtuple('_income', 'wage bonus')

    def __init__(self, name: str, surname: str, position: str, wage: int and float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.__pattern_income(wage=wage, bonus=bonus)


class Position_2(Worker_2):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return round(self._income.wage + self._income.wage * self._income.bonus, 2)


if __name__ == '__main__':
    locksmith = Position('Иван', 'Иванов', 'Слесарь 18 разряда', 150000, 0.4)
    driver = Position('Валера', 'Валерьев', 'Водитель категории С', 40231.99, 0.15)
    print(locksmith.get_full_name(), locksmith.get_total_income(), sep=' | ')
    print(driver.get_full_name(), driver.position, driver.get_total_income(), sep=' | ')
    print('Размер экземпляров:', asizeof(locksmith), asizeof(driver))

    locksmith = Position_2('Иван', 'Иванов', 'Слесарь 18 разряда', 150000, 0.4)
    driver = Position_2('Валера', 'Валерьев', 'Водитель категории С', 40231.99, 0.15)
    print(locksmith.get_full_name(), locksmith.get_total_income(), sep=' | ')
    print(driver.get_full_name(), driver.position, driver.get_total_income(), sep=' | ')
    print('Размер экземпляров:', asizeof(locksmith), asizeof(driver))

"""
Также применены слоты. Если класс не планируется расширять, применение слотов и именованного кортежа даст почти в 2 раза
экономию по памяти.

Иван Иванов | 210000.0
Валера Валерьев | Водитель категории С | 46266.79
Размер экземпляров: 1072 1080

Иван Иванов | 210000.0
Валера Валерьев | Водитель категории С | 46266.79
Размер экземпляров: 600 608
"""
