"""
Курс Основы Python, урок 9. Задание 4
Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат."""
from pympler import asizeof


class Car:
    def __init__(self, colour, name, speed, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print(self.colour, self.name, 'поехала')

    def stop_car(self):
        print(self.colour, self.name, 'остановилась')

    def go_right(self):
        print(self.colour, self.name, 'повернула направо')

    def go_left(self):
        print(self.colour, self.name, 'повернула налево')

    def show_speed(self):
        print('Текущая скорость автомобиля = ', self.speed)


class TownCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)

    def show_speed(self):
        if self.speed <= 60:
            print('Текущая скорость автомобиля = ', self.speed)
        else:
            print('Превышена допустимая скорость')


class SportCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)


class WorkCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)

    def show_speed(self):
        if self.speed <= 40:
            print('Текущая скорость автомобиля = ', self.speed)
        else:
            print('Превышена допустимая скорость')


class PoliceCar(Car):
    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed, True)


car_1 = Car('Серебристый', 'Lexus', 120)
print(f'Размер созданного объекта: ', asizeof.asizeof((car_1)))   # 592
w_car = WorkCar('Оранжевый', 'Kamaz', 40)
print(f'Размер созданного объекта: ', asizeof.asizeof((w_car)))   # 592
p_car = PoliceCar('Малиновая', 'Lada', 35)
print(f'Размер созданного объекта: ', asizeof.asizeof((p_car)))   # 600

"""Оптимизиция памяти выполнена за счёт хранения атрибутов классов в слотах. 
Итоговые замеры показали, что потребляемый объем памяти снизился за счёт оптимизации:
"""


class Car:
    __slots__ = ['colour', 'name', 'speed', 'is_police']

    def __init__(self, colour, name, speed, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print(self.colour, self.name, 'поехала')

    def stop_car(self):
        print(self.colour, self.name, 'остановилась')

    def go_right(self):
        print(self.colour, self.name, 'повернула направо')

    def go_left(self):
        print(self.colour, self.name, 'повернула налево')

    def show_speed(self):
        print('Текущая скорость автомобиля = ', self.speed)


class TownCar(Car):
    __slots__ = ['colour', 'name', 'speed']

    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)

    def show_speed(self):
        if self.speed <= 60:
            print('Текущая скорость автомобиля = ', self.speed)
        else:
            print('Превышена допустимая скорость')


class SportCar(Car):
    __slots__ = ['colour', 'name', 'speed']

    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)


class WorkCar(Car):
    __slots__ = ['colour', 'name', 'speed']

    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed)

    def show_speed(self):
        if self.speed <= 40:
            print('Текущая скорость автомобиля = ', self.speed)
        else:
            print('Превышена допустимая скорость')


class PoliceCar(Car):
    __slots__ = ['colour', 'name', 'speed']

    def __init__(self, colour, name, speed):
        super().__init__(colour, name, speed, True)


car_2 = Car('Серебристый', 'Lexus', 120)
print(f'Размер созданного объекта: ', asizeof.asizeof((car_2)))   # 272
w_car2 = WorkCar('Оранжевый', 'Kamaz', 40)
print(f'Размер созданного объекта: ', asizeof.asizeof((w_car2)))   # 296
p_car2 = PoliceCar('Малиновая', 'Lada', 35)
print(f'Размер созданного объекта: ', asizeof.asizeof((p_car2)))   # 304
