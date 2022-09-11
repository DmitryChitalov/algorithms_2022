"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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

Это файл для пятого скрипта
"""
# курс основ, урок 11, задание 1:
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

from memory_profiler import profile


@profile
def shell():
    class Date:
        string_date = ''
        day = 0
        month = 0
        year = 0

        def __init__(self, string_date):
            self.string_date = string_date

        @classmethod
        def convert_to_number(cls):
            cls.day = int(cls.string_date[:2])
            cls.month = int(cls.string_date[3:5])
            cls.year = int(cls.string_date[6:])

        @staticmethod
        def date_valid(day, month, year):
            if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2022:
                print('Дата корректна')
            else:
                print('Дата не корректна')

    Date.string_date = '10-02-2022'
    Date.convert_to_number()
    print(Date.day, Date.month, Date.year)
    print(type(Date.day), type(Date.month), type(Date.year))
    Date.date_valid(Date.day, Date.month, Date.year)


shell()


# в модифицированной версии используем слоты, для хранения атрибутов класса

@profile
def shell1():
    class Date1:
        __slots__ = ('day', 'month', 'year')

        def __init__(self, string_date):
            self.string_date = string_date

        @classmethod
        def convert_to_number(cls):
            cls.day = int(cls.string_date[:2])
            cls.month = int(cls.string_date[3:5])
            cls.year = int(cls.string_date[6:])

        @staticmethod
        def date_valid(day, month, year):
            if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2022:
                print('Дата корректна')
            else:
                print('Дата не корректна')

    Date1.string_date = '10-02-2022'
    Date1.convert_to_number()
    print(Date1.day, Date1.month, Date1.year)
    print(type(Date1.day), type(Date1.month), type(Date1.year))
    Date1.date_valid(Date1.day, Date1.month, Date1.year)


shell1()
