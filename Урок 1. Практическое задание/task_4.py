"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
def binary_search(list_, item):
    low = 0
    high = len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def get_user_data_0(user):  # Константная сложность алгоритма O(1)
    users_table = {'user_0': {'password': 'psw_0', 'status': 1},
                   'user_1': {'password': 'psw_1', 'status': 0},
                   'user_2': {'password': 'psw_2', 'status': 0}}
    dict_psw = users_table.get(user)
    return dict_psw.get('password'), dict_psw.get('status')


def get_user_data_1(user):  # Линейная сложность алгоритма O(n)
    users_table = [['user_0', 'psw_0', 1], ['user_1', 'psw_1', 0], ['user_2', 'psw_2', 0]]
    for val in users_table:
        if val[0] == user:
            return val[1], val[2]
    return None, None


def get_user_data_2(user):  # Логарифмическая сложность алгоритма O(log n)
    user_sorted_index = ['user_0', 'user_1', 'user_2', 'user_3', 'user_4', 'user_5', 'user_6', 'user_7', 'user_8']
    users_table = [['user_0', 'psw_0', 1], ['user_1', 'psw_1', 0], ['user_2', 'psw_2', 0],
                   ['user_3', 'psw_3', 1], ['user_4', 'psw_4', 0], ['user_5', 'psw_5', 0],
                   ['user_6', 'psw_6', 1], ['user_7', 'psw_7', 0], ['user_8', 'psw_8', 0]
                   ]
    index = binary_search(user_sorted_index, user)
    if index is None:
        return None, None
    return users_table[index][1], users_table[index][2]


def verify_user(user, password, num):  # работаем с одним из трех алгоритмов (num := 0,1,2)
    get_user_data = [get_user_data_0, get_user_data_1, get_user_data_2]
    psw, stat = get_user_data[num](user)
    if psw is None:
        return None
    if stat == 0:
        print('Пожалуйста, активируйте учетную запись')
    return psw == password or False  # True - доступ разрешен; False - неправильный пароль


print(f"{verify_user('user_2', 'psw_1', 0)=}")
print(f"{verify_user('user_0', 'psw_0', 1)=}")
print(f"{verify_user('user_7', 'psw_7', 2)=}")

'''
В данной задаче наибольшую эффективность имеет реализации хранилища в виде словаря - O(1)
Затем бинарный поиск в заранее отсортированном массиве - O(log n)
Затем хранение в виде вложенных списков - O(n)
'''
