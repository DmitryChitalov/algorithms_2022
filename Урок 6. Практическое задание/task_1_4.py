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
from memory_profiler import profile
from recordclass import recordclass

"""--------------------------------------------------------
1.4. Для ОПТИМИЗАЦИИ используем переменных типа recordclass
-----------------------------------------------------------"""


# Курс 'Алгоритмы'. Вебинар1.
# Задание 4.  Пользователи веб-ресурса проходят аутентификацию. В системе хранятся логин, пароль и отметка об
# активации учетной записи. Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу. При этом его
# учетка должна быть активирована. А если нет, то польз-лю нужно предложить ее пройти.

@profile
def load_user_data_old(dict_, user_table):
    for user, password, status in user_table:
        dict_.setdefault(user, {'password': password, 'status': status})
    return dict_


Record = recordclass('Record', 'user password status')


@profile
def load_user_data_opt(d, user_table):
    d.extend([Record(*i) for i in user_table])
    d.sort()
    return d


def get_user_data_old(d, user):
    return d[user]['password'], d[user]['status']


def get_user_data_opt(d, user):
    user_data = list(filter(lambda rec: rec.user == user, d))
    return user_data[0].password, user_data[0].status


def verify_user(user, password, num):  # работаем с одним из трех алгоритмов (num := 0,1)
    psw, stat = [get_user_data_old, get_user_data_opt][num]([dc, rd][num], user)
    if psw is None:
        return None
    if stat == 0:
        print('Пожалуйста, активируйте учетную запись')
    return psw == password or False  # True - доступ разрешен; False - неправильный пароль


# Проверяем, что функционал одинаковый и убираем под комментарии, чтобы не мешал
# inp = [("Иван Сергеев", 'psw1', False), ("Инна Серова", "psw2", False), ("Петр Алексеев", "psw2", True)]
# dc = load_user_data_old({}, inp)
# print(dc)
# rd = load_user_data_opt([], inp)
# print(rd)
# print(verify_user("Иван Сергеев", get_user_data_old(dc, "Иван Сергеев"), 0))
# print(verify_user("Иван Сергеев", get_user_data_opt(rd, "Иван Сергеев"), 0))

# Генерируем большой массив
number = 100000
big_inp = [(f'user_{i}', f'psw_{i}', i % 2 or False) for i in range(number, 0, -1)]
rd = load_user_data_opt([], big_inp)
dc = load_user_data_old({}, big_inp)

"""
Результаты тестов показали, что использование переменных типа recordclass из одноименного пакета дает заметную
оптимизацию по памяти.

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    56     39.5 MiB     39.5 MiB           1   @profile
    57                                         def load_user_data_opt(d, user_table):
    58     45.5 MiB      5.4 MiB      100003       d.extend([Record(*i) for i in user_table])
    59     44.9 MiB     -0.7 MiB           1       d.sort()
    60     44.9 MiB      0.0 MiB           1       return d


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    46     44.9 MiB     44.9 MiB           1   @profile
    47                                         def load_user_data_old(dict_, user_table):
    48     72.4 MiB      0.0 MiB      100001       for user, password, status in user_table:
    49     72.4 MiB     27.4 MiB      100000           dict_.setdefault(user, {'password': password, 'status': status})
    50     72.4 MiB      0.0 MiB           1       return dict_
"""
