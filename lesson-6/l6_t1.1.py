from recordclass import recordclass
from sys import getsizeof


def num_translate_adv(num):
    letter_one = num[0]
    num = num.lower()
    translate = {'zero': '"ноль"',
                 'one': '"один"',
                 'two': '"два"',
                 'three': '"три"',
                 'four': '"четыре"',
                 'five': '"пять"',
                 'six': '"шесть"',
                 'sever': '"семь"',
                 'eight': '"восемь"',
                 'nine': '"девять"',
                 'ten': '"десять"', }
    answer = translate.get(num)
    if letter_one.isupper():
        answer = answer.title()
        return answer, f'Объём занимаемой объектом dict памяти: {getsizeof(translate)} байт(а)'
    else:
        return answer, f'Объём занимаемой объектом dict памяти: {getsizeof(translate)} байт(а)'


def mod_num_translate_adv(num):
    letter_one = num[0]
    num = num.lower()
    translate = recordclass('translate', ('zero', 'one',
                                          'two', 'three', 'four', 'five', 'six', 'sever', 'eight', 'nine',
                                          'ten'))
    a = translate(zero='"ноль"',
                  one='"один"',
                  two='"два"',
                  three='"три"',
                  four='"четыре"',
                  five='"пять"',
                  six='"шесть"',
                  sever='"семь"',
                  eight='"восемь"',
                  nine='"девять"',
                  ten='"десять"', )

    my_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'sever', 'eight', 'nine',
               'ten']
    if letter_one.isupper():
        answer = a[my_list.index(num)].title()
        return answer, f'Объём занимаемой объектом dict памяти: {getsizeof(a)} байт(а)'
    else:
        return a[my_list.index(num)], f'Объём занимаемой объектом dict памяти: {getsizeof(a)} байт(а)'


num = input()
print(num_translate_adv(num))
print(mod_num_translate_adv(num))

# recordclass потребляет меньше ппамяти в сравнении с обычным словарем
# One
# ('"Один"', 'Объём занимаемой объектом dict памяти: 640 байт(а)')
# ('"Один"', 'Объём занимаемой объектом dict памяти: 104 байт(а)')
# Прошу помочь разобраться, как я могу добавлять в имя перемененной свое значение, к примеру мне нужна
# переменная a.{вводимая переменная к примеру через input} как я могу это сделать??