def recur_method(num):
    if num == 1:
        return num
    else:
        return recur_method(num - 1) + num


try:
    NUM = int(input("Введите число: "))
    if recur_method(NUM) == NUM * (NUM + 1) / 2:
        print("Равенство верно")
except ValueError:
    print("Вместо строки введите число")
