def show_least(a):
    # a = [какой-то массив, набор чисел]
    # t = сначала это первый элемент, потом мы его сравниваем до тех пор,
    # пока не найдём меньше, тогда он становится m
    t = a[0]
    for i in range(len(a)):     # O(n)
        if t > a[i]:
            t = a[i]
    return t
# Сложность: О(n)


def least_of_listed(a):
    k = len(a)
    while k != 0:               # O(n)
        for i in range(1, k):   # O(n)
            if a[i] < a[i-1]:
                p = a[i-1]
                # p обозначили удаляемый элемент, чтобы потом вставить
                # его на другое место
                del a[i-1]
                a.insert(i, p)
        k -= 1
    return a[0]
# Сложность: О(n^2)
b = [9, 4, 8, 3, 5]
print(least_of_listed(b), show_least(b))
