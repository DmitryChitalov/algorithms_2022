
def to_revert(number):
    return str(number) if number < 10 else str(number % 10) + to_revert(number // 10)

try:
    number = int(input('Введите натуральное число: '))
    print(to_revert(number))
except ValueError:
    print(f'Введен неверный формат числа!')