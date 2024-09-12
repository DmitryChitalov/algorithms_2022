def reverse_num(number: int, string=''):
    if number // 10 == 0:
        string += str(number % 10)
        return string
    string += str(number % 10)
    return reverse_num(number // 10, string)


def check_zero(reversed_num: str):
    return reversed_num[1:] + reversed_num[0]


num = int(input('Введите натуральное число'))
rev_num = reverse_num(num)
if rev_num[0] == '0':  # учет нуля как в примере
    rev_num = check_zero(rev_num)
print(f'число {num}, перевернутое {rev_num}')
