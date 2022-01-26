# По O-нотации сложность заполнения списка О(1), для заполнения словаря также О(1)
from time import perf_counter

def func(k):
    A = []
    n = 0
    start = perf_counter()
    while n != k:
        A.append(n)
        n += 1
    time1 = perf_counter() - start

    A = {}
    n = 0
    start = perf_counter()
    while n != k:
        A.setdefault(n, n + 10 * k)
        n += 1
    time2 = perf_counter() - start

    return time1 - time2

print(func(100), func(10000), func(1000000), sep='\n')
# При увеличении k увеличивается и разница во временах выполнения.
# Так просходит, потому что в словаре не должно быть коллизий,
# поэтому все ключи проверяются на идентичность с новым,
# если они разные, то добавляется новый элемент словаря.




# Для удаления и там, и там также О(1)
# А так как у нас цикл, проходящий через все значения, то и там, и там О(n)
# Разница снова увеличивается при увеличении длин списка и словаря,
# потому что при удалении ключа происходит и удаление значения
def fancy(k):
    a = []
    n = 0
    while n != k:
        a.append(n)
        n += 1

    b = {}
    n = 0
    while n != k:
        b.setdefault(n, n + 10 * k)
        n += 1

    n = 0
    start = perf_counter()
    while n != k:
        a.pop()
        n += 1
    time1 = perf_counter() - start

    n = 0
    start = perf_counter()
    while n != k:
        b.pop(n)
        n += 1
    time2 = perf_counter() - start

    return time1 - time2

print(fancy(100), fancy(10000), fancy(1000000), sep='\n')