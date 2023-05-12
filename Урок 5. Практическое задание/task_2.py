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

from collections import deque
from collections import defaultdict
from functools import reduce


def get_hex():
    hex = list(input("Type a hex number: "))
    hex = defaultdict(hex, str())
    return hex

def get_hex(n):
    hex = list(n)
    hex = deque(hex)
    return hex

DECTOHEX = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')

def sum_hex(a,b):
    #adec = int(a, 16)
    #bdec = int(b, 16)
    #return hex(adec,bdec)
    #for i in range(len(a),0,-1):
    #    a[i]
    res = []
    l = max(len(a),len(b))
    buf = int()
    for i in range(l-1,-1,-1):
        digitsum = int(a[i],16) + int(b[i],16) + buf
        buf = digitsum // 16
        num = digitsum % 16
        if num == 0 and buf == 0:
            break
        res.append(DECTOHEX[num])
    return res


def sum_hex_pair(a, b='0'):
    sum = int(a, 16) + int(b, 16)
    digit = DECTOHEX[sum % 16]
    next = DECTOHEX[sum // 16]
    digit = list(hex(digit + next)[2:])
    return digit


def red_sum(l):
    return reduce(sum_hex_pair,l)



def sum_hex2(a,b):
    l = max(len(a), len(b))
    buf = 0
    res = deque()
    dd = defaultdict(list)
    for i in range(0, l+2):
        if len(a) != 0:
            dd[i].append(a.pop())
        else:
            dd[i].append('0')
        if len(b) != 0:
            dd[i].append(b.pop())
        else:
            dd[i].append('0')
        digitsum = int(dd[i][0], 16) + int(dd[i][1], 16) + buf
        buf = digitsum // 16
        num = digitsum % 16
        if num == 0 and buf == 0:
            break
        res.appendleft(DECTOHEX[num])
    return res
    #print(reduce(sum_hex_pair, dd.values()))


class Hexadec(list):
    def __init__(self, data):
        super(Hexadec, self).__init__(reversed(data))
    def __add__(self, other):
        slen = len(self)
        olen = len(other)
        res = 0
        if slen > olen:
            for i in range(0,slen):
                res += int(self[i],16)*16**i
                if i < olen:
                    res += int(other[i],16)*16**i
        else:
            for i in range(0,olen):
                res += int(other[i],16)*16**i
                if i < slen:
                    res += int(self[i],16)*16**i
        return list(hex(res).upper()[2:])

    def __mul__(self, other):
        pass

    def __str__(self):
        return str(list(reversed(self)))

def prod_hex(a,b):
    l = max(len(a), len(b))
    buf = []
    a.reverse()
    b.reverse()
    res = 0
    dd = defaultdict(list)
    for i in range(0, len(a)):
        buf.append(0)
        for ii in range(0, len(b)):
            buf[i] += int(a[i],16)*int(b[ii],16)*(16**ii)*(16**i)
        res += buf[i]
    res = deque(hex(res).upper()[2:])
    return res



if __name__ == "__main__":
    print((15*15+14)//16)
    print(str()+'2')
    a = get_hex("A2")
    b = get_hex("C4F")
    print(a,b)
    print(sum_hex2(a.copy(), b.copy()))
    #print(red_sum([a.copy(), b.copy()]))
    print(prod_hex(a.copy(), b.copy()))
    #print(red_sum(a + b))

    a = Hexadec("A2")
    b = Hexadec("C4F")
    print(a)
    print(b)
    print(a+b)


