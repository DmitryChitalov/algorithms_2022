def sw(A):
    m = A[0]
    for i in range(len(A)):     # O(n)
        if m > A[i]:
            m = A[i]
    return m
# Сложность: О(n)

def lw(A):
    k = len(A)
    while k != 0:               # O(n)
        for i in range(1, k):   # O(n)
            if A[i] < A[i-1]:
                p = A[i-1]
                del A[i-1]
                A.insert(i, p)
        k -= 1
    return A[0]
# Сложность: О(n^2)
B = [9, 4, 8, 3, 5]
print(lw(B), sw(B))