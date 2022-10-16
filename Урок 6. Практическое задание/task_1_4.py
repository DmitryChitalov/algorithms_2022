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

Algorithms  Lesson 3 task 2
 программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api

Script listing:
Размер dict:  107944
Размер json:  39424


Анализ:
для хранения аутентификационных данных использовался словарь credential_dictionary[el],
для его долгосрочного хранения используется  JSON string    credent_dict_ser = json.dumps(credential_dictionary)
Размер dict:  107944
Размер json:  39424

для долгосрочного хранения данных размер словаря был оптимизирован.

"""

from json import loads, dumps
from pympler import asizeof

import hashlib
import json
import sys


test_names = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia', 'Isabella',
              'Mia', 'Evelyn', 'Harper', 'Luna', 'Camila', 'Gianna', 'Elizabeth', 'Eleanor', 'Ella', 'Abigail',
              'Avery', 'Scarlett', 'Emily', 'Aria', 'Penelope', 'Chloe', 'Layla', 'Mila', 'Nora', 'Hazel',
              'Madison', 'Ellie', 'Lily', 'Nova', 'Isla', 'Grace', 'Violet', 'Aurora',
              'Riley', 'oey', 'Willow', 'Emilia', 'Stella', 'Zoe', 'Victoria', 'Hannah', 'Addison', 'Leah', 'Lucy',
              'Everly', 'Lillian', 'Paisley', 'Elena', 'Naomi', 'Maya', 'Natalie', 'Kinsley', 'Delilah', 'Claire',
              'Aaliyah', 'Ruby', 'Brooklyn', 'Alice', 'Aubrey', 'Autumn', 'Leilani', 'Savannah', 'Valentina', 'Kennedy',
              'Bella', 'Skylar', 'Genesis', 'Sophie', 'Hailey', 'Sadie', 'Natalia', 'Quinn', 'Caroline', 'Allison',
              'Gabriella', 'Anna', 'Serenity', 'Nevaeh', 'Cora', 'Ariana', 'Emery', 'Lydia', 'Jade', 'Sarah', 'Eva',
              'Adeline', 'Madeline', 'Piper', 'Rylee', 'Athena', 'Peyton', 'Everleigh', 'Vivian', 'Clara', 'Raelynn',
              'Liliana', 'Samantha', 'Maria', 'Iris', 'Ayla', 'Eloise', 'Lyla', 'Eliza', 'Hadley', 'Melody',
              'Julia', 'Parker', 'Rose', 'Isabelle', 'Brielle', 'Adalynn', 'Arya', 'Eden', 'Remi',
              'Mackenzie', 'Maeve', 'Margaret', 'Reagan', 'Charlie', 'Alaia', 'Melanie', 'Josie', 'Elliana',
              'Mary', 'Daisy', 'Alina', ' Lucia', 'Ximena', 'Juniper', 'Kaylee', 'Magnolia',
              'Summer', 'Adalyn', 'Sloane', 'Amara', 'Arianna', 'Isabel', 'Reese', 'Emersyn',
              'Sienna', 'Kehlani', 'River', 'Freya', 'Valerie', 'Blakely', 'Genevieve', 'Esther', 'Valeria',
              'Katherine', 'Kylie', 'Norah', 'Amaya', 'Bailey', 'Ember', 'Ryleigh', 'Georgia',
              'Catalina', 'Emerson', 'Alexandra', 'Faith', 'Jasmine', 'Ariella', 'Ashley', 'Andrea', 'Millie',
              'June', 'Khloe', 'Callie', 'Juliette', 'Sage', 'Ada', 'Anastasia', 'Olive', 'Alani', 'Brianna',
              'Rosalie', 'Molly', 'Brynlee', 'Amy', 'Ruth', 'Aubree', 'Gemma', 'Taylor', 'Oakley',
              'Margot', 'Arabella', 'Sara', 'Journee', 'Harmony', 'Blake', 'Alaina', 'Aspen', 'Noelle',
              'Selena', 'Oaklynn', 'Morgan', 'Londyn', 'Zuri', 'Aliyah', 'Jordyn', 'Juliana', 'Finley', 'Presley',
              'Zara', 'Leila', 'Marley', 'Sawyer', 'Amira', 'Lilly', 'London', 'Kimberly', 'Elsie',
              'Ariel', 'Lila', 'Alana', 'Diana', 'Kamila', 'Nyla', 'Vera', 'Hope', 'Annie', 'Kaia', 'Myla',
              'Alyssa', 'Angela', 'Ana', 'Lennon', 'Evangeline', 'Harlow', 'Rachel', 'Gracie', 'Rowan', 'Laila',
              'Elise', 'Sutton', 'Lilah', 'Adelyn', 'Phoebe', 'Octavia', 'Sydney', 'Mariana', 'Wren',
              'Lainey', 'Vanessa', 'Teagan', 'Kayla', 'Malia', 'Elaina', 'Saylor', 'Brooke', 'Lola',
              'Miriam', 'Alayna', 'Adelaide', 'Daniela', 'Jane', 'Payton', 'Journey', 'Lilith', 'Delaney', 'Dakota',
              'Mya', 'Charlee', 'Alivia', 'Annabelle', 'Kailani', 'Lucille', 'Trinity', 'Gia', 'Tatum',
              'Raegan', 'Camille', 'Kaylani', 'Kali', 'Stevie', 'Maggie', 'Haven', 'Tessa', 'Daphne', 'Adaline',
              'Hayden', 'Joanna', 'Jocelyn', 'Lena', 'Evie', 'Juliet', 'Fiona', 'Cataleya', 'Angelina', 'Leia',
              'Paige', 'Julianna', 'Milani', 'Talia', 'Rebecca', 'Kendall', 'Harley', 'Lia', 'Phoenix', 'Dahlia',
              'Logan', 'Camilla', 'Thea', 'Jayla', 'Brooklynn', 'Blair', 'Vivienne', 'Hallie', 'Madilyn',
              'Mckenna', 'Evelynn', 'Ophelia', 'Celeste', 'Alayah', 'Winter', 'Catherine', 'Collins', 'Nina',
              'Briella', 'Palmer', 'Noa', 'Mckenzie', 'Kiara', 'Amari', 'Adriana', 'Gracelynn', 'Lauren',
              'Cali', 'Kalani', 'Aniyah', 'Nicole', 'Alexis', 'Mariah', 'Gabriela', 'Wynter', 'Amina', 'Ariyah',
              'Adelynn', 'Remington', 'Reign', 'Alaya', 'Dream', 'Alexandria', 'Willa', 'Avianna', 'Makayla',
              'Gracelyn', 'Elle', 'Amiyah', 'Arielle', 'Elianna', 'Giselle', 'Brynn', 'Ainsley', 'Aitana',
              'Charli', 'Demi', 'Makenna', 'Rosemary', 'Danna', 'Izabella', 'Lilliana', 'Melissa',
              'Samara', 'Lana', 'Mabel', 'Everlee', 'Fatima', 'Leighton', 'Esme', 'Raelyn', 'Madeleine', 'Nayeli',
              'Camryn', 'Kira', 'Annalise', 'Selah', 'Serena', 'Royalty', 'Rylie', 'Celine', 'Laura',
              'Brinley', 'Frances', 'Michelle', 'Heidi', 'Rory', 'Sabrina', 'Destiny', 'Gwendolyn',
              'Alessandra', 'Poppy', 'Amora', 'Nylah', 'Luciana', 'Maisie', 'Miracle', 'Joy', 'Liana', 'Raven',
              'Shiloh', 'Allie', 'Daleyza', 'Kate', 'Lyric', 'Alicia', 'Lexi', 'Addilyn', 'Anaya', 'Malani',
              'Paislee', 'Elisa', 'Kayleigh', 'Azalea', 'Francesca', 'Jordan', 'Regina', 'Viviana', 'Aylin',
              'Skye', 'Daniella', 'Makenzie', 'Veronica', 'Legacy', 'Maia', 'Ariah', 'Alessia', 'Carmen', 'Astrid',
              'Maren', 'Helen', 'Felicity', 'Alexa', 'Danielle', 'Lorelei', 'Paris', 'Adelina', 'Bianca',
              'Gabrielle', 'Jazlyn', 'Scarlet', 'Bristol', 'Navy', 'Esmeralda', 'Colette', 'Stephanie',
              'Jolene', 'Marlee', 'Sarai', 'Hattie', 'Nadia', 'Rosie', 'Kamryn', 'Kenzie', 'Alora', 'Holly',
              'Matilda', 'Sylvia', 'Cameron', 'Armani', 'Emelia', 'Keira', 'Braelynn', 'Jacqueline',
              'Alison', 'Amanda', 'Cassidy', 'Emory', 'Ari', 'Haisley', 'Jimena', 'Jessica', 'Elaine',
              'Dorothy', 'Mira', 'Eve', 'Oaklee', 'Averie', 'Charleigh', 'Lyra', 'Madelynn', 'Angel', 'Edith',
              'Jennifer', 'Raya', 'Ryan', 'Heaven', 'Kyla', 'Wrenley', 'Meadow', 'Carter', 'Kora',
              'Saige', 'Kinley', 'Maci', 'Mae', 'Salem', 'Aisha', 'Adley', 'Carolina', 'Sierra', 'Alma', 'Annabella'
              ]


def hash_function(input_string, input_solt):
    hash_obj = hashlib.sha256(str(input_solt).encode() + str(input_string).encode())
    return hash_obj.hexdigest()


credential_dictionary = {}


def credential_dict_generator():
    for i, el in enumerate(test_names):
        el_passw = 100000 + i
        credential_dictionary[el] = hash_function(el_passw, el)


def serialization():
    credent_dict_ser = json.dumps(credential_dictionary)
    return credent_dict_ser


def new_user_creation(usr_login):
    inp_passw = input(' Please enter password : ')
    user_hash = hash_function(inp_passw, usr_login)
    credential_dictionary[usr_login] = user_hash
    print(f' New user created')


credential_dict_generator()
dict_ser = serialization()

print('Размер dict: ', asizeof.asizeof(credential_dictionary))
print('Размер json: ', asizeof.asizeof(dict_ser))

if __name__ == '__main__':
    inp_login = input('please enter your login: ')
    if inp_login in credential_dictionary:
        inp_passw = input('please enter your password: ')
        print(f'    Hash generated from Password     : {hash_function(inp_passw, inp_login)}')
        print(f'    Stored hash for user {inp_login} : {credential_dictionary[inp_login]}')
        if hash_function(inp_passw, inp_login) == credential_dictionary[inp_login]:
            print(f' -- Authentication success -- ')
            sys.exit(0)
        else:
            print(f' -- Authentication fails -- ')
            sys.exit(0)
    else:
        new_user_creation(inp_login)
