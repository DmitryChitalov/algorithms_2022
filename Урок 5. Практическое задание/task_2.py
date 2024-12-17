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

from typing import Callable, Any, List

# Получаем данные из ввода
dictionary = {}
for num in range(1, 3):
    hex_num = input(f"Введите {num}-e число: ")
    dictionary[f'{num}-{hex_num}'] = list(hex_num)

# Функция для преобразования шестнадцатеричного числа в десятичное
to_int = lambda x: int(''.join(x), 16)

# Функция применяющая метод и возвращающая список из элементов строчного представления
# получившегося числа в шестнадцатиричной системе счисленияю
result_list: Callable[[Any, Any, Any], List[str]] = lambda x, y, method: list(f"{method(x, y):X}")

print(f"Сумма введённых чисел:"
      f"{result_list(*map(to_int, dictionary.values()), int.__add__)}")

print(f"Произведение введённых чисел:"
      f"{result_list(*map(to_int, dictionary.values()), int.__mul__)}")

"""Второй вариант решения с использованием ООП."""


class Hexadecimal:
    """
    Класс для создания списка представления шестнадцатеричных чисел
    в виде списка умножения и сложения.
    """

    def __init__(self, hex_num: list):
        self.hex_num = hex_num

    # Преобразуем в десятичную систему счисления
    def _to_int(self: list) -> int:
        num_to_int = int(''.join(self.hex_num), 16)
        return num_to_int

    # Суммируем числа
    def __add__(self, other: list) -> list:
        result = self._to_int() + other._to_int()
        return list(f"{result:X}")

    # Умножаем числа
    def __mul__(self, other: list) -> list:
        result = self._to_int() * other._to_int()
        return list(f"{result:X}")

    # Строковое представление числа
    def __repr__(self) -> str:
        return f"{self.hex_num}"


# Получение список всех значений из словаря и преобразование
# в экземпляры класса Hexadecimal
number_1, number_2 = map(Hexadecimal, dictionary.values())

print("Создал экземпляры класса Hexadecimal и выполнил необходимые операции"
      "используя ранее введённые данные")
print(f"Сумма чисел: {number_1 + number_2}")
print(f"Произведение чисел: {number_1 * number_2}")
