def recur_method(numb):
    if numb == 1:
        return numb
    else:
        return recur_method(numb - 1) + numb


try:
    NUMB = int(input("Введите число: "))
    if recur_method(NUMB) == NUMB * (NUMB + 1) / 2:
        print('Равенство верно')
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")

"""
def recur_method(base):
    '''Через тернарный оператор'''
    return base if base == 1 else base + recur_method(base - 1)

n = 3
print(f'Is 1+2+...+{n} = {n}({n}+1/2? \nAnswer: '
      f'{recur_method(n) == n * (n + 1) / 2} (Sum = {recur_method(n)})')
"""