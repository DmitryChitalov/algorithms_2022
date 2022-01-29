"""Для создания хешей паролей эффективное решение
Так называемый парольный хеш
"""

from hashlib import pbkdf2_hmac
from binascii import hexlify

# Здесь мы создаем хеш sha256 в пароле при помощи соли со 100,000 итераций.
obj = pbkdf2_hmac(hash_name='sha256',
                         password=b'any_password',
                         salt=b'any_salt_1',
                         iterations=100000)


print(obj)  # -> b'n\x97\xba\xd2\x1fb\x00\xf9\x08p6\xa7\x1e|
# \xa9\xfa\x01\xa5\x9e\x1di\x7f~\x02\x84\xcd\x7f\x9b\x89}|\x02'

# это значение можно записать в БД
result = hexlify(obj)
# result = type(obj)

print(result)  # -> b'6e97bad21f6200f9087036a71e7ca9fa
# 01a59e1d697f7e0284cd7f9b897d7c02'
