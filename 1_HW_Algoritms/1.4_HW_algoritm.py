"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


#  первое решение  O(1)
def authentication(users_data, database):
      if users_data in database.keys() and database.get(users_data) == 0:                 # O(1)
            return print(f'Привет {users_data[0]}, тебе нужно пройти активацию ')         # O(1)
      elif users_data in database.keys() and database.get(users_data) == 1:               # O(1)
            return print(f'привет {users_data[0]}, делай все что пожелаешь')              # O(1)
      else:
            return print(f'учетная запись не найдена')                                    # O(1)


users = {
      ('qwerty', '12345'): 0,
      ('bob', '656565'): 1,                                                               # O(1) так как известно кол-во
      ('tom', '3333'): 0
}

login = tuple(input("Введите логин и пароль через пробел: ").split())                     # O(1)

authentication(login, users)                                                              # O(1)


# второе решение O(n)

def authentication2(users_data, database):
      for key, value in database.items():                                                 # O(n)
            if key == users_data:                                                         # O(1)
                  if value == 1:                                                          # O(1)
                        return print('Доступ разрешен')                                   # O(1)
                  elif value == 0:                                                        # O(1)
                        return print('нужно активироать акаунт')                          # O(1)
            else:                                                                         # O(1)
                  return print('Логин или пароль не найден')                              # O(1)


authentication2(login, users)                                                             # O(1)

#  первое решение эфеткивнее. Хранилище выполнено в словаре, что позволяет быстро
#  искать пользователя (хэш). Причем ключем является кортеж с логином и паролем. Кортеж не изменяемый тип данных
#  как раз подходит для хранении логина и пароля, а значение является меткой активации (информация, которая меняется)