from time import time


def decorrator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(time() - start)
        return result
    return timer


################################### A
# заполнить список
@decorrator
def a_list(llist, element): # O(1)
    llist.append(element)
    return llist

@decorrator
def a_dict(ddict, key, value): # O(1)
    ddict[key] = value
    return ddict


ll = [1, 5, 2, 3, 8, "2345", "dfg", True]
d = {1: 'asd', 2: "qwe"}
print(a_list(ll, 'asd'))
print(a_dict(d, 3, "rty"))
################################### A

print("___")

################################### B
# взять элемент
@decorrator
def b_list(llist, index): # O(1)
    return llist[index]

@decorrator
def b_dict(ddict, key): # O(1)
    return ddict[key]


ll = [1, 5, 2, 3, 8, "2345", "dfg", True]
d = {1: 'asd', 2: "qwe", 345: "sdfsf", "sdfd": 1234}
print("b - ", b_list(ll, 5))
print("b - ", b_dict(d, 1))
################################### B

print("___")

################################### C
# удалить элемент
@decorrator
def c_list(llist, element): # O(N)
    llist.remove(element)
    return llist

@decorrator
def c_dict(ddict, key): # O(N)
    del ddict[key]
    return ddict


ll = [1, 5, 2, 3, 8, "2345", "dfg", True]
d = {1: 'asd', 2: "qwe", 345: "sdfsf", "sdfd": 1234}
print("c - ", c_list(ll, "2345"))
print("c - ", c_dict(d, 1))
################################### C
