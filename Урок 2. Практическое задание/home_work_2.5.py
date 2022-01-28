def chr_row(ascii_val=32):

    if ascii_val == 128:
        return True
    print(f'{ascii_val} - {chr(ascii_val)}', end=' ')
    if (ascii_val - 31) % 10 == 0:
        print('\n')

    chr_row(ascii_val + 1)


chr_row()
