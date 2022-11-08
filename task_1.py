from collections import Counter


def call():
    try:
        n = int(input('Введите количество предприятий для расчета прибыли: '))
    except ValueError:
        print('Введите число!'), call()
    res = Counter()
    for i in range(n):
        name = input('Введите название предприятия: ')
        a = input('Через пробел введите прибыль\nза 4 квартала данного предприятия: ').split()
        ls = []
        for j in a:
            ls.append(float(j))
        b = sum(ls)
        res[name] = b
    res['middle'] = sum(res.values()) / len(res)
    print('---------------------')
    print(f'Средняя годовая прибыль всех предприятий: {res["middle"]:.2f}')
    top = res.most_common().index(('middle', res['middle']))
    print('Предприятия, с прибылью выше среднего значения:', *dict(res.most_common()[:top]).keys())
    print('Предприятия, с прибылью ниже среднего значения:', *dict(res.most_common()[top+1:]).keys())


call()
