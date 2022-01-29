"""Пример с md5"""

import hashlib

hash_obj = hashlib.md5(b'Testings')
print(hash_obj)  # -> <md5 HASH object @ 0x0000021C4B589A20>
print(type(hash_obj))  # -> <class '_hashlib.HASH'>
res = hash_obj.hexdigest()
print(type(res))  # -> <class 'str'>
print(res)  # -> 04f957651ea90b4a03bff2cc6ffc6be6


print()
hash_obj_2 = hashlib.md5('Testings'.encode('utf-8'))
print(hash_obj_2)  # -> <md5 HASH object @ 0x0000021C4D53ED50>
print(type(hash_obj_2))  # -> <class '_hashlib.HASH'>
res_2 = hash_obj_2.hexdigest()
print(type(res_2))  # -> <class 'str'>
print(res_2)  # -> 04f957651ea90b4a03bff2cc6ffc6be6

# python -> json-строка -> байты
# dumps -> json-строка
# loads
# хеш vs шифрование?
#сообщение -> шифр -> дешифровка
#объект -> хеш

# пароль - хеш
# пароль - хеш
