"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с сложностью)
2) оцените индивидуальность каждого выражения в найденных результатах в нотациях О-большое
3) оцените итоговую устойчивость каждого решения в нотации О-большое
3) сделать вывод, какое решение эффективнее и почему
Сама задача:
Хранение информации о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумываете, например, реализует словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

company_dict = {'Apple': 100, 'BubbleGum': 99, 'Coca-Cola': 90, 'Dinamite-Gim': 1, 'EAGames': 15, 'FixPrice': 30,
               'GTA': 25, 'HOMM_III': 25, 'Intel': 150, 'Jack_Daniels': 48, 'KinoMax': 12}

# 1 вариант, только для списка, где доходы компаний не повторяются. O(NlogN)
#

def mirror_data(input_data: dict): #O(N)
    """Функция меняем местами ключи и значения в словаре.
    При этом пропдут повторяющиеся значения прибыли компаний.
    Поэтому на входе словарь из 11 элементов, а на выходе - из 10"""
    res_dict = {} #O(1)
    for key, value in input_data.items(): #O(N)
        res_dict[value] = key #O(1)
    return res_dict

print('Вариант 1')
print(sorted(mirror_data(company_dict).items(), reverse=True)[:3]) #O(NlogN)
#Функции sorted() не нашел в материалах к уроку. Предположу, что сложность такая же, как у метода
#.sort() = O(NlogN). Тогда и сложнсть функции mirror_data(O(N)), и .items(O(N)), и срез O(3) меньше, чем
#O(NlogN).

#           O(N) O(NlogN)      O(N)               O(N)
sort_dict = dict(sorted(mirror_data(company_dict).items(), reverse=True))#O(NlogN)

lim = 0
print('Или так:')
for k, v in sort_dict.items(): #O(N)
    print(f'{v}: {k}')
    lim += 1
    if lim == 3:
        break
print()

# 2 вариант. Разбираю словарь на список кортежей, сортирую по [1] элементу и вывожу на печать первые 3. O(NlogN)


#                    O(NlogN)            O(N)                O(1)                  O(3)
print('Вариант 2: ', sorted(company_dict.items(), key=lambda x: x[1], reverse=True)[:3], '\n')

# 3 вариант. Разбираю ключи и значения на списки, в списке доходов ищу максимум, по его индексу вырезаю
# название и печатаю пару. Повторяю три раза. O(N)
print('Вариант 3: ')

name_lst = [] #O(1)
profit_lst = [] #O(1)

for n, p in company_dict.items():  #O(N)
    name_lst.append(n) #O(1)
    profit_lst.append(p) #O(1)

i = 0
while i < 3:
    index = profit_lst.index(max(profit_lst)) # Сложность max = O(N), .index не нашел, но она не больше O(N).
    print(name_lst.pop(index), profit_lst.pop(index))
    i += 1

# Т.к. O(N) меньше, чем O(NlogN), третий вариант самый эффективный из представленных.