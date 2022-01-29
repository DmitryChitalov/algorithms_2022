"""Хеширование и соль"""

# Модуль uuid применяется для генерации случайного числа
from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 80740ba2a1584aa7bf96d32bbe774e54
salt = 'my_salt'
print(type(salt))
print(type(salt))

passwd = "programmer"
# соль-часть хеша
res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
# -> efbb20c297f52672a5211f1358ad8d72907f56e1ff24cd67a6e8b4683a6a18d2
print(res)

# sha1, md5 - ненадежные
# пароли одинаковые
# логины строго разные. user2, user3 - логины уникальные
# 1111 - своя
# 1111
