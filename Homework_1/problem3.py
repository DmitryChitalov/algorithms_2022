def sw(B):
    C = []
    A = B
    for l in range(3):              # O(1)
        for i in range(len(A)):     # O(n)
            m = A[0]
            if m[1] < A[i][1]:
                m = A[i]
        C += [m[0]]
        A.remove(m)
    return C
# Сложность: O(n)

def lw(B):
    A = B
    k = len(A)
    while k != 0:                   # O(n)
        for i in range(1, k):       # O(n)
            if A[i][1] < A[i-1][1]:
                p = A[i-1]
                del A[i-1]
                A.insert(i, p)
        k -= 1
    return A[-1][0], A[-2][0], A[-3][0]
# Сложность: O(n^2)
B = [['A', 4], ['B', 6], ['C', 8], ['D', 5]]
print(lw(B), sw(B))