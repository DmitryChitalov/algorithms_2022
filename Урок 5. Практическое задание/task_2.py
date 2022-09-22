from collections import defaultdict

dict_1 = defaultdict(list)


class HexNumOper:
    def __init__(self, num):
        self.num = num
        self.num_hex = hex(int(num, 16))
        self.num_hex_arr = [char.upper() for char in str(self.num_hex)[2:]]
        self.sum_arr = []

    def __add__(self, other):
        sum_hex = hex(int(self.num, 16) + int(other.num, 16))
        sum_arr = [char.upper() for char in str(sum_hex)[2:]]
        return sum_arr

    def __mul__(self, other):
        mul_hex = hex(int(self.num, 16) * int(other.num, 16))
        mul_arr = [char.upper() for char in str(mul_hex)[2:]]
        return mul_arr


def fill_dict(num):
    num_str = str(hex(int(num, 16)))[2:]
    num_arr = [char.upper() for char in num_str]
    dict_1[num].append(num_arr)


first_num = input("Введите первое число:   ")
second_num = input("Введите второе число:   ")

print("___________Вариант с defaultdict_______________ ")

fill_dict(first_num)
fill_dict(second_num)

sum1 = str(hex(int(first_num, 16) + int(second_num, 16)))[2:]
mul1 = str(hex(int(first_num, 16) * int(second_num, 16)))[2:]

fill_dict(sum1)
fill_dict(mul1)

print(f"Первое число: {dict_1[first_num][0]} \n Второе число: {dict_1[second_num][0]} \n "
      f"Сумма чисел: {dict_1[sum1][0]} \n Произведение чисел:  {dict_1[mul1][0]} ")

print("___________Вариант с ООП_______________ ")

first_num2 = HexNumOper(first_num)
second_num2 = HexNumOper(second_num)

print(f"Первое число: {first_num2.num_hex_arr} \n Второе число: {second_num2.num_hex_arr} \n "
      f"Сумма чисел: {first_num2 + second_num2} \n Произведение чисел:  {first_num2 * second_num2} ")