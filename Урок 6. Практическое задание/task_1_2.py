"""
Задание 1.2.
"""
# Алгоритмы Python. DZ_4.3
# Приведен код, формирующий из введенного числа
# обратное по порядку входящих в него цифр и вывести на экран.


from memory_profiler import memory_usage


def mem_usage(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение функции заняло {mem_diff} Mib")
        return res

    return wrapper


@mem_usage
def func(enter_num):
    return ''.join(reversed(str(enter_num)))


@mem_usage
def func_opt(enter_num):
    yield reversed(str(enter_num))


n = 123456789

if __name__ == '__main__':
    func(n)
    func_opt(n)

"""
Выполнение функции заняло 0.0078125 Mib
Выполнение функции заняло 0.0 Mib

При использование оператора yield мы не сохраняем в памяти промежуточные
результаты. Сразу всё идёт на выход функции.
При больших объёмах входных данных, может-быть не очень быстро, 
но экономит память.
"""
