from collections import namedtuple

def sum(lst):
    n = 0
    for i in lst:
        n += int(i)
    return n
Come = namedtuple("Come", "name come")

earn_list = []
n = int(input("Enter quantity of companies: "))
for i in range(n):
    earn_list += [Come(input("Enter company name: "), sum(input("Enter incomes by every Q: ").split()) / 4)]

avg = 0
for i in earn_list:
    avg += i[1] / n

less = []
more = []
for i in earn_list:
    if i[1] < avg:
        less += [i[0]]
    else:
        more += [i[0]]

print("Companies with less income than avg: ", end='', sep='')
print(*less, sep=', ')
print("Companies with more income than avg: ", end='', sep='')
print(*more, sep=', ')
