"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""
# Урок 1, задание 4

from pympler.asizeof import asizeof
from recordclass import recordclass

# исходное решение
dict_user = {'login1': ['1234', False], 'login2': ['134', False], 'login3': ['234', True], 'login4': ['1234', False]}

def check_user_1(dict_user, login_in, pass_in): # O(n)
# последовательно проверить для каждого пользователя    
    for login in dict_user.keys(): # O(n)
        if login == login_in: # O(1)
            if dict_user[login][1]: # O(1)
                if dict_user[login][0] == pass_in: # O(1)
                    return 'Допущен' # O(1)
                else:
                    return 'Ошибка в логине или пароле' # O(1)
            else:
                return 'Активируйте аккаунт' # O(1)
    return 'Неизвестный логин' # O(1)

print(check_user_1(dict_user, '', ''))
print(check_user_1(dict_user, 'login1', ''))
print(check_user_1(dict_user, 'login3', ''))
print(check_user_1(dict_user, 'login3', '234'))
print('Размер dict_user:', asizeof(dict_user))

# Оптимизация - пароль и признак активации хранятся в record
user_class = recordclass('user_class', ('passsw', 'activated'))
dict_user_rec = {}
dict_user_rec['login1'] = user_class(passsw='1234', activated=False)
dict_user_rec['login2'] = user_class(passsw='134', activated=False)
dict_user_rec['login3'] = user_class(passsw='234', activated=True)
dict_user_rec['login4'] = user_class(passsw='1234', activated=False)

print('--- После оптимизации')
print(check_user_1(dict_user, '', ''))
print(check_user_1(dict_user, 'login1', ''))
print(check_user_1(dict_user, 'login3', ''))
print(check_user_1(dict_user, 'login3', '234'))
print('Размер dict_user_rec:', asizeof(dict_user_rec))

# Результат - уменьшился объём использованной памяти
