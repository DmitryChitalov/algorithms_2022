import hashlib

# соль сгенерирована и сохранена для пользовтаеля
salt = b''
# ключ мы уже ранее расчитали и "записали" в базу данных
key = b'\xeb\xe3\xb1\xcc\xc8\x16d\x84\xe6\xa0\xde@' \
      b'\xdc\xa8\xc18k\n\x8bI[C.ww\x9d\xc2L \xda^\x96'

# пароль, указанный пользователем
password_to_check = 'my_pass'
 

new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'),
    salt,
    100000
)

if new_key == key:
    print('Пароль верный')
else:
    print('Пароль неверный')
