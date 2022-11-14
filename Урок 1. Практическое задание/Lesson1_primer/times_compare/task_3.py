"""Проверка сложности"""

# первые три присваивания - это константа (3) 3+300+20+1
VAL_A = 5
VAL_B = 6
VAL_C = 10
# три присваивания выполняются n^2 раз внутри вложенной итерации (3n^2)
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j

# n=3 for I in range(n): print(i)

# два присваивания, повторяющиеся n раз (2n)
for k in range(10):
    w = VAL_A*k + 45
    v = VAL_B*VAL_B
# последний оператор присваивания (1)
VAL_D = 33

# T(n)=3+3n^2+2n+1=3n**2+2n+4
# O(n**2)


def f(n):
    res = max(list(range(n))) # O(n)
    a = 1  # O(1)
    return res # O(1)
