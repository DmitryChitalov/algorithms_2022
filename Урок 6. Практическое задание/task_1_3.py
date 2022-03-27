"""
Задание 1.

Это файл для третьего скрипта
"""


"""2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного
кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;"""

from pympler import asizeof


# Не оптимизированная
class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def weight(self):
        return f'{(self.length * self.width * 25 * 5) / 1000} тонн'


r_1 = Road(28, 5155)
print(asizeof.asizeof(r_1))


# Оптимизировання
class Road2:
    __slots__ = ['length', 'width']

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def weight(self):
        return f'{(self.length * self.width * 25 * 5) / 1000} тонн'


r_2 = Road2(28, 5155)
print(asizeof.asizeof(r_2))


"""
С помощью слотов выйграли по памяти в три раза

Результаты: 1 - 328
            2 - 112
"""