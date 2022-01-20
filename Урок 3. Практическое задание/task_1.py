"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import hashlib
from binascii import hexlify

print(10)
object = hashlib.pbkdf2_hmac(hash_name='sha256', 
   password=b'123',
   salt=b'salt',
   iterations=1000000)

print(hexlify(object))

# Продвинутая хэш функция:
hashlib.pbkdf2_hmac(hash_name='sha256', 
   password=b'123',
   salt=b'salt',
   iterations=1000000)
# Преобразовать в строку для базы данных:
from binascii import hexlify
print(hexlify(object))
# генерация случайных байтов:
os.urandom()
# генерация случайного числа:
uuid4.uuid4()
salt = uuid4().hex

res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)

from sys import getsizeof
from pympler.asizeof import asizeof


d = {1: '1', 2: '2', 3: '3'}
print(getsizeof(d))  # -> 240
print(asizeof(d))  # -> 504

t = (1, 2, 3)
print(getsizeof(t))  # -> 72
print(asizeof(t))  # -> 168
