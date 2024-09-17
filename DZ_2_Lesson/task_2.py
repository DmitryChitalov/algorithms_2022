def ch_and_nch(num, list_1, list_2):
    len_num = len(list(str(num))) # считаем длину числа
    if len_num == 1:
        if num % 2 == 0:
            list_1.append(num)
            return list_1, list_2
        else:
            list_2.append(num)
            return list_1, list_2

    now_num = num - (10 ** (len_num - 1)) * (num // (10 ** (len_num - 1))) # все что не первая цифра

    if ((num - now_num) / (10 ** (len_num - 1))) % 2 == 0: # если первая цифра четная
        list_1.append(int(((num - now_num) / (10 ** (len_num - 1)))))
    else:
        list_2.append(int(((num - now_num) / (10 ** (len_num - 1)))))

    if now_num == 0:
        return now_num, list_1, list_2
    return ch_and_nch(now_num, list_1, list_2)


print(ch_and_nch(19235360659530, [], []))