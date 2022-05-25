

# O(n)
def min_value_first(lst: list) -> int:
    min_value = lst[0]          # O(1)
    for el in lst:              # O(n)
        if el < min_value:      # O(1)
            min_value = el      # O(1)
    return min_value            # O(1)


# O(n^2)
def min_value_second(lst: list) -> int:
    min_value = lst[0]                  #O(1)
    for el in lst:                      #O(n)
        if el < min_value:              #O(1)
            for i in lst:               #O(n)
                if el<i:                #O(1)
                    min_value = i       #O(1)
    return min_value                    #O(1)
