
#Задание 7. На закрепление навыков работы с деком

from test import DequeClass

def pal_checker(string):
    dc_obj = DequeClass()

    if string.capitalize():
        string=string.lower()


    if " " in string:
        string = string.replace(" ", "")

    for el in string:

        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal

print(pal_checker("А роза упала на лапу Азора"))