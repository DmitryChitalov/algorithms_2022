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

profiles = {
    'User1': ['12344', False],
    'Sorcer': ['qwerty', False],
    'Bond': ['mypassword', True],
    'Doomguy': ['iddqd', False],
    'VVG81': ['180381', True],
}


# Решение №1. Сложность: O(2)
def check_activation(name):
    if profiles[name][1] == False:  # O(1) + O(1)
        return (f'{name}, вам необходимо пройти активацию')
    else:
        return (f'Добро пожаловать, {name}')


print(check_activation('Sorcer'))
print(check_activation('Bond'))


# Решение №2. Сложность: O(n) + O(4)
def check_activation_2(name):
    for key in profiles.keys():  # O(n)
        if key == name:  # O(1) + O(1)
            if profiles[name][1] == False:  # O(1) + O(1)
                return f'{name}, вам необходимо пройти активацию'
            else:
                return f'Добро пожаловать, {name}'


print(check_activation_2('Doomguy'))
print(check_activation_2('VVG81'))

# решение №1 более лаконичное и менее сложное.
