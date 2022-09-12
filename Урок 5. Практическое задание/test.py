
from collections import namedtuple, deque


tuple_companies = namedtuple('Enterprises', 'name_company, quarter_1, quarter_2, sum')
quarter_1 = int(input("Введите прибыль за 1 квартал: "))
quarter_2 = int(input("Введите прибыль за 2 квартал: "))
print(type(quarter_2))
sum = quarter_1 + quarter_2
companies = tuple_companies(name_company=input('Введите название предприятия:'),
                            quarter_1=quarter_1,
                            quarter_2=quarter_2,
                            sum=sum)
print(companies)
