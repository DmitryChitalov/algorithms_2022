"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    num = str(enter_num)
    res = ''.join(reversed(num))
    return res


number = 2433425252432

"""
В первой функции используется рекурсия, но это не самый быстрый способ, так как он проходится по всем цифрам числа, 
и затем в обратном порядке возвращая числа.
Врмя выполнения: 0.01410 
"""
print(revers(number))
print(fr"Замер revers:{timeit('revers(number)', globals=globals(), number=1000)}")

"""
Во второй функции используется цик while, здесь сразу берется последнее число и приписывается к результату,
цикл повторяется пока число не будет равно 0.
Этот способ самый быстрый
Время выполнения: 0.00756
"""
print(revers_2(number))
print(fr"Замер revers_2: {timeit('revers_2(number)', globals=globals(), number=1000)}")

"""
В третьей функции используется срез, для использования стреза число необходимо преобразовать в строку,
и записать результат среза.
этот способ самый медленный, так как операции со строками потребляют больше ресурсов.
Время выполнения: 2.84999
"""
print(revers_3(number))
print(fr"Замер revers_3: {timeit(revers_3(number), globals=globals(), number=1000)}")

"""
В четвертой функции я использовал встроеную функциию reversed, 
для её использования так же нужно было преоброзовать число в строку,
и выполнить reversed. операции со строками более затраны по времени по этому в 4-й функции, 
время выполнения самое медленное как и в 3-й функции.
Время выполнения: 2.84999
"""
print(revers_4(number))
print(fr"Замер revers_4: {timeit(revers_4(number), globals=globals(), number=1000)}")
