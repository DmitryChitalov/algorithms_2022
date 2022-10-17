def ascii(start=32, end=127):
    if (start + 9) % 10 == 0:
        print(f'{start} - {chr(start)}', end='\n')
    else:
        print(f'{start} - {chr(start)}', end=' ')
    if start == end:
        return True
    ascii(start + 1)

ascii()