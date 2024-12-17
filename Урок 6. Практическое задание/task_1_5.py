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

Это файл для пятого скрипта
Задание взял из Урок 5, task_2.
"""
"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
"""
Первый вариант решения.
Не увидел смысла, необходимости в использовании collections.defaultdict, reduce
"""
from memory_profiler import memory_usage
from timeit import timeit


# Определяем декоратор для измерения используемой памяти и подсчета затрачиваемого времени
def count_memory_usage(func):
    """Counts memory usage and time usage of a function."""

    def wraper(*args, **kwargs):
        mem_usage_before = memory_usage()[0]
        result = func(*args, **kwargs)
        result_time = timeit(lambda: func(*args, **kwargs), number=10000)
        mem_usage_after = memory_usage()[0]
        print(f"Использовано памяти: {mem_usage_after - mem_usage_before} MiB")
        print(f"Затрачено времени: {result_time} секунд")
        return result

    return wraper


dictionary = {'1 - A2': 'A2', '2 - C4F': 'C4F'}


# Класс без __slots__.
class Hexadecimal:
    """
    Класс для создания списка представления шестнадцатеричных чисел
    в виде списка умножения и сложения.
    """

    def __init__(self, hex_num: str):
        self.hex_num = list(hex_num)

    # Преобразуем в десятичную систему счисления.
    def _to_int(self) -> int:
        num_to_int = int(''.join(self.hex_num), 16)
        return num_to_int

    # Суммируем числа.
    def __add__(self, other) -> list:
        result = self._to_int() + other._to_int()
        return list(f"{result:X}")

    # Умножаем числа.
    def __mul__(self, other) -> list:
        result = self._to_int() * other._to_int()
        return list(f"{result:X}")

    # Строковое представление числа.
    def __repr__(self) -> str:
        return f"{self.hex_num}"


# Класс с __slots__.
class HexadecimalWithSlots:
    __slots__ = ['hex_num']

    def __init__(self, hex_num: str):
        self.hex_num = list(hex_num)

    # Преобразуем в десятичную систему счисления.
    def _to_int(self) -> int:
        num_to_int = int(''.join(self.hex_num), 16)
        return num_to_int

    # Суммируем числа.
    def __add__(self, other) -> list:
        result = self._to_int() + other._to_int()
        return list(f"{result:X}")

    # Умножаем числа.
    def __mul__(self, other) -> list:
        result = self._to_int() * other._to_int()
        return list(f"{result:X}")

    # Строковое представление числа.
    def __repr__(self) -> str:
        return f"{self.hex_num}"


# Пример теста с декоратором.
@count_memory_usage
def test_memory_usage(hex1: str, hex2: str) -> list:
    return Hexadecimal(hex1) + Hexadecimal(hex2)


@count_memory_usage
def test_memory_usage_with_slots(hex1: str, hex2: str) -> list:
    return HexadecimalWithSlots(hex1) + HexadecimalWithSlots(hex2)


# Запуск тестов без __slots__.
test_memory_usage(*dictionary.values())
# Запуск тестов с __slots__.
test_memory_usage_with_slots(*dictionary.values())

"""
Уменьшение потребления памяти. Использование __slots__ позволяет существенно уменьшить потребление памяти,
 так как исключается создание словаря для каждого экземпляра.
Увеличение скорости. Несмотря на то, что основное улучшение связано с памятью,
 исключение словаря также может улучшить производительность, особенно при больших объёмах данных,
  поскольку доступ к атрибутам осуществляется быстрее.
Профилирование показало, что потребление памяти снизилось после добавления __slots__. Сравнивая результаты до и после, вы сможете увидеть разницу в потребляемой памяти.
Заключение
Оптимизация с __slots__ позволяет значительно уменьшить использование памяти,
особенно когда количество объектов велико.
Применение memory_profiler помогает наглядно увидеть улучшения.
"""
