from collections import deque

all_sum = deque()
just_dict = {}
b_pred = []
m_pred = []
r_pred = []

count = int(input("колличество предприятий: "))

for i in range(int(count)):
    need_list = []
    name = input("название предприятия: ")
    money = input("прибыль за 4 квартала(через пробел): ")
    ll = money.split(" ")
    for i in ll:
        all_sum.appendleft(int(i))
        need_list.append(int(i))
    just_dict[name] = sum(need_list)/4

summ = (sum(all_sum))/(4*count)

for i in just_dict:
    if just_dict[i] > summ:
        b_pred.append(i)
    elif just_dict[i] < summ:
        m_pred.append(i)
    else:
        r_pred.append(i)

print("Средняя годовая прибыль всех предприятий -", summ)
print("Предприятия чья прибыль больше среднего значения -", *b_pred)
print("Предприятия чья прибыль меньше среднего значения -", *m_pred)
print("Предприятия чья прибыль равна среднему значению -", *r_pred)