def sum_elem(elem, sum=0, next_num=1):
    if elem == 0:
        return sum
    else:
        sum += next_num
        return sum_elem(elem-1, sum, next_num / -2)


test_1 = sum_elem(3)
print(test_1)
