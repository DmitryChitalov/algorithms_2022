company_list = {"nnn": 123000, "gharlder": 457070, "grobn": 123110, "flader": 475674, "alcal": 2345254, }

def alg_one(llist): # O(N)
    list_wty = []

    for i in llist:
        list_wty.append(llist.get(i))

    first_big = max(list_wty) # O(N)
    list_wty.remove(first_big) # O(N)
    second_big = max(list_wty) # O(N)
    list_wty.remove(second_big) # O(N)
    third_big = max(list_wty) # O(N)
    list_wty.remove(third_big) # O(N)

    return first_big, second_big, third_big # O(1)

def alg_two(llist): # O(N log N)
    list_wty = []

    for i in llist:
        list_wty.append(llist.get(i))

    list_wty.sort()

    return list_wty[-1], list_wty[-2], list_wty[-3]

print(alg_one(company_list))
print(alg_two(company_list))