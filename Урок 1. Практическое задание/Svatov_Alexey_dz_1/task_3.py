"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
company_profit = dict([('Apple', 57411000000),
                       ('Saudi Aramco', 49287000000),
                       ('SoftBank Group', 47053000000),
                       ('Industrial & Commercial Bank of China', 45783000000),
                       ('Microsoft', 44281000000),
                       ('Berkshire Hathaway', 42521000000),
                       ('Alphabet', 40269000000),
                       ('China Construction Bank', 39283000000),
                       ('Agricultural Bank of China', 31293000000),
                       ('Facebook', 29146000000),
                       ('JPMorgan Chase & Co.', 29131000000),
                       ('Bank of China', 27952000000),
                       ('Tencent Holdings', 23166000000),
                       ('Alibaba Group Holding', 22224000000),
                       ('Samsung Electronics', 22116000000),
                       ('Amazon', 21331000000),
                       ('Toyota Motor', 21180000000),
                       ('Intel', 20899000000),
                       ('Ping An Insurance', 20739000000),
                       ('Bank of America Corp.', 17894000000),
                       ('Verizon Communications', 17801000000),
                       ('Taiwan Semiconductor Manufacturing', 17344000000),
                       ('UnitedHealth Group', 15403000000),
                       ('Roche Group', 15229000000),
                       ('Johnson & Johnson', 14714000000),
                       ('China Merchants Bank', 14108000000),
                       ('Sanofi', 14031000000),
                       ('Walmart', 13510000000),
                       ('Nestlé', 13031000000),
                       ('Procter & Gamble', 13027000000),
                       ('China Mobile Communications', 12920000000),
                       ('Home Depot', 12866000000),
                       ('Fannie Mae', 11805000000),
                       ('Bank of Communications', 11409000000),
                       ('Cisco Systems', 11214000000),
                       ('Sony', 11054000000),
                       ('Citigroup', 11047000000),
                       ('Morgan Stanley', 10996000000),
                       ('ThyssenKrupp', 10725000000),
                       ('Comcast', 10534000000),
                       ('Сбербанк', 10527000000),
                       ('Oracle', 10135000000),
                       ('Volkswagen', 10104000000),
                       ('Rio Tinto Group', 9769000000),
                       ('Industrial Bank', 9656000000),
                       ('Pfizer', 9616000000),
                       ('Goldman Sachs Group', 9459000000),
                       ('Huawei Investment & Holding', 9362000000),
                       ('Toronto-Dominion Bank', 8841000000),
                       ('Nippon Telegraph and Telephone', 8643000000)])


def top_3_company_profit_v1(company_dict):  # O(N^2 + 2N) - квадратичная
    _dict = company_dict.copy()  # O(N)
    top_3_company_profit = {}  # O(N)
    count = 0  # O(1)
    for name, profit in _dict.items():  # O(N)
        if (profit == max(_dict.values())) and (name not in top_3_company_profit.keys()):  # O(N)
            top_3_company_profit.update([(name, profit)])  # O(1)
            _dict[name] = 0  # O(1)
            count += 1  # O(1)
            if count == 3: # O(1)
                break # O(1)
    return top_3_company_profit  # O(1)


def top_3_company_profit_v2(company_dict):  # O(7N) - линейная
    re_company_dict = {profit: name for name, profit in company_dict.items()}  # O(N)
    result = ''  # O(1)
    for i in range(0, 3):  # O(3)
        _profit = max(re_company_dict.keys())  # O(N)
        _name = re_company_dict.pop(max(re_company_dict.keys()))  # O(N)
        result += f'Компания: {_name}, прибыль: {_profit}\n'  # O(1)
    return result # O(1)


def top_3_company_profit_v3(company_dict): # O(2N) - линейная
    re_company_dict = {profit: name for name, profit in company_dict.items()}  # O(N)
    sort_top_3_company_list = sorted(re_company_dict.keys(), reverse=True)[0:3] # O(N)
    result = f'Компания: {re_company_dict.get(sort_top_3_company_list[0])}, прибыль: {sort_top_3_company_list[0]},\n' \
             f'Компания: {re_company_dict.get(sort_top_3_company_list[1])}, прибыль: {sort_top_3_company_list[1]},\n' \
             f'Компания: {re_company_dict.get(sort_top_3_company_list[2])}, прибыль: {sort_top_3_company_list[2]},\n' # O(1)
    return result # O(1)


print(f'result_v1 \n {top_3_company_profit_v1(company_profit)} \n')
print(f'result_v2 \n{top_3_company_profit_v2(company_profit)} \n')
print(f'result_v3 \n{top_3_company_profit_v3(company_profit)} \n')
# for name, profit in company_profit.items():
