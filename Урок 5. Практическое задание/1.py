dct = {x: x**2 for x in range(0,20)}
print(dct)

def del_dct(dct):
    for x in range(5,10):
        del dct[x]
    return dct
print(del_dct(dct))