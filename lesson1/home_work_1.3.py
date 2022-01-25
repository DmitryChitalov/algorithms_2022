company = {'Cola': 30000, 'Pepsi': 10000, 'Fanta': 70000, 'Sprite': 120000}
print(len(company))


# Первый способ. Сложность O(n log n)
def price_value_1(item):
    return item[1]                                                          # O(1)


max_price_1 = {}                                                            # O(1)
i = 0                                                                       # O(1)
for k, v in sorted(company.items(), key=price_value_1, reverse=True):       # O(n + n log n)
    if i < 3:                                                               # O(n)
        max_price_1.setdefault(k, v)                                        # O(1)
    i = i + 1                                                               # O(1)
print(max_price_1)                                                          # O(1)


# Второй способ. Сложность O(n)
def price_value_2(company):                                                # O(n)
    max_price_2 = {}                                                       # O(1)
    list_d = dict(company)                                                 # O(1)
    for n in range(3):                                                     # O(1)
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])              # O(n)
        del list_d[maximum[0]]                                             # O(1)
        max_price_2[maximum[0]] = maximum[1]                               # O(1)
    print(max_price_2)                                                     # O(1)


price_value_2(company)                                                     # O(1)


# Второй вариант O(n) будет лучше, чем первый O(n log n), так как имеет меньшую вычислительную сложность.