"""
комментарий после проверки:
здесь мы исп-ем ф-строки
"""


def symbols(n=32, count=0):
    print(f"{str(n)} - {chr(n)} ", end='')
    n += 1
    count += 1
    if n <= 127 and count <= 9:
        return symbols(n, count)
    elif n <= 128 and count > 9:
        count = 0
        print()
        return symbols(n, count)


symbols()
