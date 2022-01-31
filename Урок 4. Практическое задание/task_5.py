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


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def simple_2(i):
    """С использованием «Решета Эратосфена»"""
    count = 1
    start = 3
    end = i**2
    sieve = [el for el in range(start, end) if el % 2 != 0]
    prime = [2]
    if i == 1:
        return 2
    while count < i:
        for el in range(len(sieve)):
            if sieve[el] != 0:
                count += 1
                if count == i:
                    return sieve[el]
                j = el + sieve[el]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[el]
        prime.extend([el for el in sieve if el != 0])
        start, end = end, end + i**2
        sieve = [el for el in range(start, end) if el % 2 != 0]
        for el in range(len(sieve)):
            for num in prime:
                if sieve[el] % num == 0:
                    sieve[el] = 0
                    break


if __name__ == '__main__':
    import cProfile

    i = int(input('Введите порядковый номер искомого простого числа: '))


    def main():
        simple(i)
        simple_2(i)

    cProfile.run('main()')

# В текущем виде кумулятивное время выполнение функции с решетом Эрастофена немного больше, чем у наивного варианта.
# С точки зрения простоты кода - выгоднее наивный вариант. При этом время работы без учета вложенных функций
# выгодно отличает вариант с решетом. Если потребуется поиск по "большим" индексам, то первый вариант оптизировать
# проблемативно (он и так простой). В то же время код решетом Эрастофена можно оптимизировать под крупные аргументы
# функции.


