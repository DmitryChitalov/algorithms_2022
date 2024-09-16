"""Конвертация"""


from stack import StackClass

sc_obj = StackClass()


def convert_to_str(n, base_val):
    convert_str = "0123456789ABCDEF"

    while n > 0:
        if n < base_val:
            sc_obj.push_in(convert_str[n])
        else:
            sc_obj.push_in(convert_str[n % base_val])
        # стек пополняется и достигает длины 4
        print(sc_obj.stack_size())
        n = n // base_val

    res = ""
    while not sc_obj.is_empty():
        res = res + str(sc_obj.pop_out())
    return res


print(convert_to_str(5, 2))
# здесь стек уже пустой. все возвраты выполнены
print(sc_obj.stack_size())
