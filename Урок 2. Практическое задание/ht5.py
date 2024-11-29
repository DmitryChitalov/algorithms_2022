
def my_func(ascii_num=32):
    if ascii_num == 128:
        return
    print(f'{ascii_num} - {chr(ascii_num)}', end=' ')
    if ascii_num % 10 == 1:
        print('\n')
    my_func(ascii_num + 1)

my_func()