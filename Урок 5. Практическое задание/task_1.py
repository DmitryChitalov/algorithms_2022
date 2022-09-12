"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
#from collections import Counter
from collections import namedtuple


list_of_companies = []
companies = namedtuple("CompanyIncome", "name quartal_1 quartal_2 quartal_3 quartal_4 total quartal_average")



def digital_array(array):
    """Проверяет содержит ли массив digits методом перебора. Возвращает False как только находит элемент, который non-digit;
    возвращает True, если все элементы массива digits"""
    flag = True
    for el in array:
        if el.isdigit():
            flag = True
        else:
            flag = False
            return flag
    return flag


def get_companies():
    lst_companies = []
    companies = input('Введите название компаний через пробел: ').split(' ')
    checked_companies = [el for el in companies if el != '']

    for el in checked_companies:
        lst_companies.append(el)

    return lst_companies


def get_income(lst):
    for el in lst:
        while True:
            income = input(f'Введите через пробел выручку по кварталам для {el}: ').split(' ')
            checked_income = [el for el in income if el != '']
            if len(checked_income) == 4 and digital_array(checked_income):
                income = [int(el) for el in checked_income]
                break
            else:
                print('Вы ввели ошибочные данные. Необходимо ввести четыре числа через пробел')

        company = companies(name=el, quartal_1=income[0], quartal_2=income[1], quartal_3=income[2],
                            quartal_4=income[3], total=income[0] + income[1] + income[2] + income[3],
                            quartal_average=(income[0] + income[1] + income[2] + income[3])/4)
        list_of_companies.append(company)
    return list_of_companies

def average_year(lst):
    total = 0
    for i in range(len(lst)):
        total = total + lst[i].total
    return total/len(lst)

def min_income(lst):
    array = []

    for i in range(len(lst)):
        if lst[i].total < average_year(lst):
            array.append(lst[i].name)
    return array

def max_income(lst):
    array = []

    for i in range(len(lst)):
        if lst[i].total > average_year(lst):
            array.append(lst[i].name)

    return array


lst = get_income(get_companies())

print(average_year(lst))
print(f'Предприятия с выручкой ниже средней: {min_income(lst)}')
print(f'Предприятия с выручкой выше средней: {max_income(lst)}')
print(f'Среднеквартальная выручка "{lst[0].name}" составила {lst[0].quartal_average}')

