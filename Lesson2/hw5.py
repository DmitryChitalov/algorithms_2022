def get_symbol(ascii=32):
    if ascii == 128:
        return True
    print(f'{ascii} - {chr(ascii)}', end=' ')
    if (ascii - 31) % 10 == 0:
        print('\n')
    get_symbol(ascii + 1)


get_symbol()
