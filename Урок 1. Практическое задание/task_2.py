from random import randint


def search_min(lst):  # O(n^2)
    min_val = 10 ** 6  # O(1)
    for ind, num in enumerate(lst):  # O(n)
        for j in lst[ind+1:]:  # O(n)
            if j <= num and j < min_val:  # O(1)
                min_val = j  # O(1)
            elif j >= num and num < min_val:  # O(1)
                min_val = num  # O(1)
    return min_val  # O(1)


def search_min_v2(lst):  # O(n)
    min_val = 10 ** 6  # O(1)
    for i in lst:  # O(n)
        if i < min_val:  # O(1)
            min_val = i  # O(1)
    return min_val  # O(1)


some_list = [randint(-50, 50) for _ in range(10)]

print(min(some_list))
print(search_min(some_list))
print(search_min_v2(some_list))
