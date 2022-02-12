"""Профилировка затрат памяти"""

from math import sqrt
from memory_profiler import profile


@profile
def get_prime_numbers(count):
    prime_numbers = [2]
    next_number = 3

    while len(prime_numbers) < count:
        if is_prime(next_number, prime_numbers):
            prime_numbers.append(next_number)
        next_number += 1

    return prime_numbers


@profile
def is_prime(num, prime_numbers):
    limit = int(sqrt(num)) + 1
    for i in prime_numbers:
        if i > limit:
            break
        if num % i == 0:
            return False
    return True


get_prime_numbers(5)


# Проблем с памятью нет. Всё в пределах нормы.
