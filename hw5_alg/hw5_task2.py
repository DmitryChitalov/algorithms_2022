from collections import defaultdict

dictionary = defaultdict(tuple)
x = input('1 число в 16ричной СС ')
y = input('2 число в 16ричной СС ')
dictionary[x] = tuple(x)
dictionary[y] = tuple(y)
add = int(x, 16) + int(y, 16)
add = str(hex(add)).split('x')[1].upper()  # т к иначе выводится в формате 0x...
dictionary[add] = tuple(add)
multiply = int(x, 16) * int(y, 16)
multiply = str(hex(multiply)).split('x')[1].upper()
dictionary[multiply] = tuple(multiply)
print(dictionary)
