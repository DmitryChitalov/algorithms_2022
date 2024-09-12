
from task_14 import DequeClass # оставил как было, класс не привожу здесь


def pal_checker(string):
    dc_obj = DequeClass()

    string_2 = string.split()
    string_2 = ''.join(string_2)
    for el in string_2:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))