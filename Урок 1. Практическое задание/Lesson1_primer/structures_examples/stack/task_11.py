from task_10 import StackClass


def divide_by_two(dec_number):
    sc_obj = StackClass()

    while dec_number > 0:
        res = dec_number % 2
        sc_obj.push_in(res)
        dec_number = dec_number // 2

    bin_string = ""
    while not sc_obj.is_empty():
        bin_string = bin_string + str(sc_obj.pop_out())

    return bin_string


print(divide_by_two(233))
