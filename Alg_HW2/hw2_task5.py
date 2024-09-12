def print_ascii(k: int):
    if k < 128:
        if k % 10 != 1:
            print(f'{k} - {chr(k)} ', end='')
        else:
            print(f'{k} - {chr(k)}\n')
        return print_ascii(k+1)


i = 32
print_ascii(i)
