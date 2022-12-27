from memory_profiler import profile


@profile
def memory():
    def my_sum(n):
        if n == 1:
            return 1
        else:
            return my_sum(n-1) + n

    n= int(input())
        
    if n > 0:
        if my_sum(n) == n*(n+1)/2:
            (print('выражения равны'))
        else:
            (print('не равны'))
                

memory()

@profile
def memory_2():
    def my_sum(n):
        n =int(input())
        res = 0
        for i in range(1,n+1):
            res += i
        print(res)
    

        if n > 0:
            if res == n*(n+1)/2:
                (print('выражения равны'))
            else:
                (print('не равны'))
    my_sum(200)
memory_2()
                
#переход от рекурсии к циклу 
#2 урок 7 задание (текущий курс)


