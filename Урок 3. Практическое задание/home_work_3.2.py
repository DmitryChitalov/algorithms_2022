from uuid import uuid4
import hashlib

salt = uuid4().hex


password_1 = input("Введите пароль: ")
res_1 = hashlib.sha256(salt.encode() + password_1.encode()).hexdigest()
print(res_1)

password_2 = input("Введите этот же пароль ещё раз: ")
res_2 = hashlib.sha256(salt.encode() + password_2.encode()).hexdigest()
print(res_2)

if res_1 == res_2:
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели НЕправильный пароль')
