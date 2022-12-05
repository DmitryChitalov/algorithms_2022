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
from pympler import asizeof
# дз 9 задание 4 основы
# оптимизированное


class Car:
    __slots__ = ['is_police', 'speed', 'color', 'name']

    def __init__(self, speed: int, color: str, name: str, is_police: bool = True):

        self.is_police = is_police
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:

        speed_ = self.speed + 15
        print(f'Машина {self.name} повысила скорость на 15: {speed_}')

    def stop(self) -> None:

        print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:

        if direction == 'направо':
            print(f'{self.name}: движется {direction}')
        elif direction == 'налево':
            print(f'{self.name}: движется {direction}')
        elif direction == 'прямо':
            print(f'{self.name}: движется {direction}')
        elif direction == 'назад':
            print(f'{self.name}: движется {direction}')
        else:
            raise ValueError

    def show_speed(self) -> None:

        print(f'{self.name}: текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self) -> None:
        if self.speed > 60:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self) -> None:
        if self.speed > 40:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


class PoliceCar(Car):

    def show_speed(self) -> None:
        # self.is_police = True
        # if self.is_police:
        #     print('Вруби мигалку и забудь про скорость!')
        if self.is_police:
            print('Вруби мигалку и забудь про скорость!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


# неоптимизированное


class Car_2:

    def __init__(self, speed: int, color: str, name: str, is_police: bool = True):

        self.is_police = is_police
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:

        speed_ = self.speed + 15
        print(f'Машина {self.name} повысила скорость на 15: {speed_}')

    def stop(self) -> None:

        print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:

        if direction == 'направо':
            print(f'{self.name}: движется {direction}')
        elif direction == 'налево':
            print(f'{self.name}: движется {direction}')
        elif direction == 'прямо':
            print(f'{self.name}: движется {direction}')
        elif direction == 'назад':
            print(f'{self.name}: движется {direction}')
        else:
            raise ValueError

    def show_speed(self) -> None:

        print(f'{self.name}: текущая скорость {self.speed}')


class TownCar_2(Car_2):
    def show_speed(self) -> None:
        if self.speed > 60:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


class SportCar_2(Car_2):
    pass


class WorkCar_2(Car_2):
    def show_speed(self) -> None:
        if self.speed > 40:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


class PoliceCar_2(Car_2):

    def show_speed(self) -> None:
        # self.is_police = True
        # if self.is_police:
        #     print('Вруби мигалку и забудь про скорость!')
        if self.is_police:
            print('Вруби мигалку и забудь про скорость!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


town_car = TownCar(41, "red", 'WW_Golf')
town_car_2 = TownCar_2(41, "red", 'WW_Golf')

print(asizeof.asizeof(town_car))
print(asizeof.asizeof(town_car_2))
# 360
# 560
"""
__slots__ уменьшает расход памяти для хранения аттрибутов
"""