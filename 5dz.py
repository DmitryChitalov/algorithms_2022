from memory_profiler import profile


@profile
def recursion():
    print('введите n:')
    n = int(input())
    def sum(n):
        if n == 1:
            return 1
        else:
            return sum(n-1) + (-0.5) ** (n-1)



    print(f'(Введите количество элементов: {n}')
    print(f'Количество элементов - {n}, их сумма - {sum(n)}')



@profile
def replacement_re():
    print('введите n:')
    n = int(input())
    def sum_elem(n):
        e = 1
        s = 0
        for i in range(n):
            s += e
            e /=-2
        print(sum_elem(s))
        
        
recursion()
replacement_re()
#2 урок задание 7 (текущий курс)