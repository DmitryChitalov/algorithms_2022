from statistics import mean
from collections import defaultdict

COUNT = int(input("Введите количество предприятий для расчета прибыли:\n"))
D_DICT = defaultdict(int)

for i in range(COUNT):
    company = input("Введите название предприятия:\n")
    quarterly_profit = input("Введите через пробел введите прибыль данного "
                             "предприятия за каждый квартал "
                             "(всего 4 квартала):\n")
    D_DICT[company] = mean([int(el) for el in quarterly_profit.split(" ")])

AVG_PROFIT = round(mean(D_DICT.values()), 3)

print(f"Средняя годовая прибыль всех предприятий: {AVG_PROFIT}.")
print(f"Предприятия, с прибылью выше среднего значения: "
      f"{', '.join([el for el in D_DICT.keys() if D_DICT[el] > AVG_PROFIT])}.")
print(f"Предприятия, с прибылью ниже среднего значения: "
      f"{', '.join([el for el in D_DICT.keys() if D_DICT[el] < AVG_PROFIT])}.")