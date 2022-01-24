"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (в материалах есть его описание)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
"""


from timeit import repeat, default_timer

def simple(number_simple,  *args, **kwargs):
    """Без использования «Решета Эратосфена»"""
    counter_for_simple = 1
    curent_simple_num = 2
    while counter_for_simple <= number_simple:
        divider = 1
        is_simple = True
        while divider <= curent_simple_num:
            if (curent_simple_num % divider == 0 and 
                                    divider != 1 and 
                                    divider != curent_simple_num):
                is_simple = False
                break
            divider += 1
        if is_simple:
            if counter_for_simple == number_simple:
                break
            counter_for_simple += 1
        curent_simple_num += 1
    return curent_simple_num

def sieve_of_Eratosthenes(number_simple, cache_on=False):
    """ 
    1)Создаем начальный словарь (1) простых чисел dict_simple с некоторым 
    количеством простых чисел, что во-первых позволяет вернуть результат 
    мгновенно при ввода небольшого номера простого числа,
    а во-вторых инициализирует шаг расширения словаря.
    Применен словарь из-за возможности удаления элементов за время O(1).
    2) Далее инициализируем словарь чисел(2), числа для которого находятся 
    в интервале от числа максимального простого в словаре номер (1), 
    до удвоенного значения нижней границы.
    Для словаря чисел (2) берем только нечетные числа, так как четные 
    брать не имеет смысла.
    Множитель также начинаем с 3, так как на предыдущем шаге отсеяли 
    все четные числа.
    3) После отсевания дополняем словарь простых чисел (1) оставшимися числами 
    из словаря (2)
    Первое простое число равное двум не включается в словарь (1), из-за того 
    что все четные из всех расчетов исключаются, и нет смысла каждый 
    раз брать первое нечетное равное двум для исключения чисел.
    Из-за выше указанного ввод первого простого числа учтен в самом начале.
    Также использования кэша ускоряет поиск простых чисел.
    Результаты замеров:
    simple --- num=1 --- min_time =                   5.00003807246685e-07
    ===========================================================================
    sieve_of_Eratosthenes --- num=1 --- min_time =    2.00001522898674e-07
    ===========================================================================
    simple --- num=10 --- min_time =                  1.5099998563528061e-05
    ===========================================================================
    sieve_of_Eratosthenes --- num=10 --- min_time =   7.5999414548277855e-06
    ===========================================================================
    simple --- num=1000 --- min_time =                0.2650204000528902
    ===========================================================================
    sieve_of_Eratosthenes --- num=1000 --- min_time = 0.0007599999662488699
    ===========================================================================
    На всем интервале входных чисел алгоритм решета Эратосфена работает
    быстрее наивного алгоритма, причем при больших чисел
    выигрыш значительно увеличивается.
    """
    if number_simple == 1:
        return 2
    
    if not cache_on or 'dict_simple'not in sieve_of_Eratosthenes.__dir__():
        sieve_of_Eratosthenes.dict_simple = {2: 3, 3: 5, 4: 7, 5: 11}

    dict_simple = sieve_of_Eratosthenes.dict_simple
    max_num_simple = max(dict_simple)
    while number_simple > max_num_simple:
        min_dict_num = dict_simple[max_num_simple]
        max_dict_num = min_dict_num * 2
        dict_num = {num: None for num in range(min_dict_num+2, max_dict_num, 2)}

        for current_simple in dict_simple.values():
            multiplier = 3 
            number_for_del = current_simple * multiplier
            while min_dict_num+2 <= number_for_del < max_dict_num: 
                if number_for_del in dict_num:
                    del dict_num[number_for_del]
                multiplier +=  2
                number_for_del = current_simple * multiplier

        for num_simple, simple in enumerate(dict_num, max_num_simple+1):
            dict_simple[num_simple] = simple 
  
        max_num_simple = max(dict_simple)  

    return  dict_simple[number_simple]


funcs = []

funcs.append("simple")
funcs.append("sieve_of_Eratosthenes")

num = 1
for i in range(1, 4):
    for func in funcs:
        print(f'{f"{func} --- {num=} --- min_time = ":50}'+
            str(min(repeat(f'{func}(num, cache_on=False)', default_timer, globals=globals(), repeat=3, number=1))))
        print('='*75)
    num *= 10**i





