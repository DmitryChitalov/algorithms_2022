from memory_profiler import profile

@profile
def func(n):
    def invert(n):
        if n < 10:
            return str(n)
        else:
            return str(n % 10) + invert(n // 10)
    return str(n % 10) + invert(n // 10)

'''
Так как функция рекурсивная, то количество таблиц с замерами соответствует количеству вызовов
Что бы получить одну таблицу с общим замером, оборачиваем функцию другой функцией и её уже замеряем.
'''