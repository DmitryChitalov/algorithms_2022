from pympler import asizeof

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

#неоптимизированное решение (9.4, основы python)

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала!'

    def stop(self):
        return f'{self.name} остановилась!'

    def turn(self, direction):
        return f'{self.name} повернула {direction}!'

    def show_speed(self):
        return f'Текущая скорость {self.name}:{self.speed} км/ч'

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейской машиной!'
        else:
            return f'Автомобиль {self.name} не является полицейской машиной!'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч. Допустимая скорость превышена!'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч. Допустимая скорость превышена!'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

c1 = WorkCar(70,'Красная', 'Ауди', False)
c2 = TownCar(70, 'черная', 'бмв', False)
c3 = PoliceCar(100, "белый", "Форд", True)
c4 = TownCar(40, 'черная', 'Ниссан', False)

#оптимизированное решение
class Car_2:
    __slots__ = ['speed', 'color', 'name', 'is_police']
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала!'

    def stop(self):
        return f'{self.name} остановилась!'

    def turn(self, direction):
        return f'{self.name} повернула {direction}!'

    def show_speed(self):
        return f'Текущая скорость {self.name}:{self.speed} км/ч'

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейской машиной!'
        else:
            return f'Автомобиль {self.name} не является полицейской машиной!'
class TownCar_2(Car):
    __slots__ = ['speed', 'color', 'name', 'is_police']
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч. Допустимая скорость превышена!'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч.'


class SportCar_2(Car):
    __slots__ = ['speed', 'color', 'name', 'is_police']
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar_2(Car):
    __slots__ = ['speed', 'color', 'name', 'is_police']
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч. Допустимая скорость превышена!'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч.'

class PoliceCar_2(Car):
    __slots__ = ['speed', 'color', 'name', 'is_police']
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

b1 = WorkCar_2(70,'Красная', 'Ауди', False)
b2 = TownCar_2(70, 'черная', 'бмв', False)
b3 = PoliceCar_2(100, "белый", "Форд", True)
b4 = TownCar_2(40, 'черная', 'Ниссан', False)

print('Cоздание экземпляров класса заняло:')
print(f'{asizeof.asizeof(c1)} Mib')
print(f'{asizeof.asizeof(c2)} Mib')
print(f'{asizeof.asizeof(c3)} Mib')
print(f'{asizeof.asizeof(c4)} Mib')

print('Cоздание экземпляров класса с использованием слотово заняло:')
print(f'{asizeof.asizeof(b1)} Mib')
print(f'{asizeof.asizeof(b2)} Mib')
print(f'{asizeof.asizeof(b3)} Mib')
print(f'{asizeof.asizeof(b4)} Mib')

"""Использование слотов позволяет сохранить атрибуты в менее затратном
 по памяти контейнере – списке, кортеже. 608 Mib против 416 Mib """


