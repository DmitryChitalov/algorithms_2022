def recur_method(i, num, n_count, common_sum):

    if i == n_count:
        print(f"Количество элементов: {n_count}, их сумма {common_sum}")
    elif i < n_count:
        return recur_method(i + 1, num / 2 * -1, n_count, common_sum + num)


try:
    N_COUNT = int(input("Введите количество элементов: "))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("Вместо строки введите число: ")
