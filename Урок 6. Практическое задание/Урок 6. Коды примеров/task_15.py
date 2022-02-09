"""
Выигрыш в использовании памяти дает использование форматированной строки вместо
конкатенации, так как не происходит аллокация памяти
(выделение блока памяти в куче) под временные строки,
когда поочередно конкатенируем строки.
"""


from memory_profiler import profile


@profile
def format_str(a, b, c, d, e):
    res = f'{a}_{b}_{c}_{d}_{e}_{a}_{b}_{c}_{d}_{a}_{b}'
    return res


@profile
def concat_str(a, b, c, d, e):
    res = (a + '_' + b + '_' + c + '_' + d + '_' + e + '_'
           + a + '_' + b + '_' + c + '_' + d + '_' + a + '_' + b)
    return res


concat_str('one' * (10 ** 4), 'two' * (10 ** 3),
           'three' * (10 ** 3), 'four' * (10 ** 3), 'five' * (10 ** 3))
format_str('one' * (10 ** 4), 'two' * (10 ** 3),
           'three' * (10 ** 3), 'four' * (10 ** 3), 'five' * (10 ** 3))

"""
Line #    Mem usage    Increment   Line Contents
================================================
    11     35.7 MiB     35.7 MiB   @profile
    12                             def concat_str(a, b, c, d, e):
    13     35.8 MiB      0.2 MiB       res = (a + '_' + b + '_' + c + '_' 
    + d + '_' + e + '_' + a + '_' + b + '_' + c + '_' + d + '_' + a + '_' + b)
    14     35.8 MiB      0.0 MiB       return res



Line #    Mem usage    Increment   Line Contents
================================================
     5     35.8 MiB     35.8 MiB   @profile
     6                             def format_str(a, b, c, d, e):
     7     35.8 MiB      0.0 MiB       res = f'{a}_{b}_{c}_{d}_{e}
                                                    _{a}_{b}_{c}_{d}_{a}_{b}'
     8     35.8 MiB      0.0 MiB       return res
"""
