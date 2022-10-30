from pympler import asizeof

"""
Задание из курса основ Python.
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей
дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного
кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_of_asphalt(self):
        massa_asph = self.length * self.width * 25 * (5 / 1000)
        return f'{massa_asph} тонн'


road = Road(10, 1500)
print(road.mass_of_asphalt())
print(f'Общий размер объекта road = {asizeof.asizeof(road)} байт')


class Road_2:
    __slots__ = ['length', 'width']

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_of_asphalt(self):
        massa_asph = self.length * self.width * 25 * (5 / 1000)
        return f'{massa_asph} тонн'


road_2 = Road_2(10, 1500)
print(road_2.mass_of_asphalt())
print(f'Общий размер объекта road_2 = {asizeof.asizeof(road_2)} байт')

"""
1875.0 тонн
Общий размер объекта road = 328 байт
1875.0 тонн
Общий размер объекта road_2 = 112 байт
"""
"""
При исрользовании __slots__ количество используемой памяти уменьшается
"""
