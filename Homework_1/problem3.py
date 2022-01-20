def show_largest(h):
    c = []
    a = h
    m = a[0]
    for l in range(3):              # O(1)
        for i in range(len(a)):     # O(n)
            m = a[0]
            if m[1] < a[i][1]:
                m = a[i]
        c += [m[0]]
        а.remove(m)
    return c
# Сложность: O(n)


def largest_of_listed(l):
    a = l
    k = len(a)
    while k != 0:                   # O(n)
        for i in range(1, k):       # O(n)
            if a[i][1] < a[i-1][1]:
                p = a[i-1]
                del a[i-1]
                a.insert(i, p)
        k -= 1
    return a[-1][0], a[-2][0], a[-3][0]
# Сложность: O(n^2)
b = [['A', 4], ['B', 6], ['C', 8], ['D', 5]]
print(largest_of_listed(b), show_largest(b))