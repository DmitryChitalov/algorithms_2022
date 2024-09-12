def summarize(n):
    if n < 0:
        return 0
    return n + summarize(n - 1)


k = 7
left = summarize(k)
right = k * (k + 1) / 2
if right == left:
    print('Тождество работает')
else:
    print('Левая и правая часть нетождественны')
