# не догадалась, как сделать табличный вывод по 10 элементов

def ascii_table(ascii_start):
    if ascii_start == 129:
        return
    else:
        print(f'{ascii_start} - {chr(ascii_start)}')
        return ascii_table(ascii_start+1)


test = ascii_table(32)
print(test)
