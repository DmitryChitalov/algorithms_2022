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

Это файл для третьего скрипта
"""

'''
Курс Основы языка Python.
Задание:
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''
from pympler import asizeof


def slow_down_msg(name, speed, max_allowed_speed):
    msg = f'Current speed of {name} is equal to {speed}. ' \
          f'Maximum allowed speed is equal to {max_allowed_speed}.\n' \
          f'Please slow down.'
    return msg


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} is going')

    def stop(self):
        print(f'Car {self.name} is stopped')

    def turn(self, direction):
        print(f'Car {self.name} turns {direction}')

    def show_speed(self):
        print(f'Current speeed of {self.name} is equal to {self.speed}')


class TownCar(Car):
    max_allowed_speed = 60

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_allowed_speed:
            print(slow_down_msg(self.name, self.speed, self.max_allowed_speed))
        else:
            car.show_speed()


class CarNew:
    __slots__ = ['speed', 'color', 'name', 'is_police']

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} is going')

    def stop(self):
        print(f'Car {self.name} is stopped')

    def turn(self, direction):
        print(f'Car {self.name} turns {direction}')

    def show_speed(self):
        print(f'Current speeed of {self.name} is equal to {self.speed}')


class TownCarNew(CarNew):
    max_allowed_speed = 60

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_allowed_speed:
            print(slow_down_msg(self.name, self.speed, self.max_allowed_speed))
        else:
            car.show_speed()


town_car_1 = TownCar(50, 'blue', 'Ford')
town_car_2 = TownCarNew(50, 'blue', 'Ford')

print(asizeof.asizeof(town_car_1))
print(asizeof.asizeof(town_car_2))

# полностью все задание переносить сюда не стал (дочерние классы SportCar, WorkCar, PoliceCar и т.д.), т.к.
# чтобы увидеть релультат оптимизации, достаточно данной части кода
# с помощью __slots__ удалось значительно уменьшить размер объекта класса
