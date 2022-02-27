import collections

# не понял зачем именно нам нужно хранить значения в списках, ведь можно просто дать ответ(сумму и произведение чисел)

default_dict = collections.defaultdict()

# user_1 = input("первое число: ")
# user_2 = input("второе число: ")

user_1 = "a2"
user_2 = "c4f"

default_dict[user_1] = list(user_1)
default_dict[user_2] = list(user_2)

print("сумма -", list(hex(int(user_1, 16) + int(user_2, 16)))[2:])
print("произведение -", list(hex(int(user_1, 16) * int(user_2, 16)))[2:])


class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        new = A(self.x)
        new.x += other.x
        return new

    def __mul__(self, other):
        new = A(self.x)
        new.x *= other.x
        return new

    def __str__(self):
        return str(self.x)


abc1 = A(int(user_1, 16))
abc2 = A(int(user_2, 16))
summ = str(abc1 + abc2)
div = str(abc1 * abc2)
print("сумма -", list(hex(int(summ)))[2:])
print("произведение -", list(hex(int(div)))[2:])
