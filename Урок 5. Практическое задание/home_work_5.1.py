from collections import namedtuple


def calc():
    my_var = "Company"
    n = int(input("Введите количество компаний: "))
    companies = namedtuple(
        my_var,
        " name period_1 period_2 period_3 period_4")
    profit_aver = {}
    for i in range(n):
        company = companies(
            name=input("Введите название предприятия: "), period_1=int(
                input("Введите прибыль за первый квартал: ")), period_2=int(
                input("Введите прибыль за второй квартал: ")), period_3=int(
                input("Введите прибыль за третий квартал: ")), period_4=int(
                input("Введите прибыль за четвертый квартал: ")))

        profit_aver[company.name] = (
                                            company.period_1 + company.period_2 +
                                            company.period_3 + company.period_4) / 4

    total_aver = 0
    for value in profit_aver.values():
        total_aver += value
    total_aver = total_aver / n

    for key, value in profit_aver.items():
        if value > total_aver:
            print(f"{key} - прибыль выше среднего")
        elif value < total_aver:
            print(f"{key} - прибыль ниже среднего")
        elif value == total_aver:
            print(f"{key} - средняя прибыль")


calc()
