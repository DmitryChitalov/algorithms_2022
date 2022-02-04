# Дмитрий, так и не пойму, как же мне вытащить значения в случае с recordclass. В документации указано,
# что значения можно получить либо по инлексу, либо по конкретному имени вроде rc_values.zero, а мне же нужно
# передать сюда значение, которое вводит пользователь.

'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
'''
from recordclass import recordclass
from memory_profiler import profile

num_translation = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


# @profile()
def num_translate(num):
    return num_translation.get(num.lower()).capitalize() if num[0].isupper() else num_translation.get(num.lower())


# print(num_translate('five'))
# print(num_translate('fifty'))


nums_rc = recordclass('nums_dict', ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
rc_values = nums_rc(zero='ноль', one='один', two='два', three='три', four='четыре', five='пять',
                    six='шесть', seven='семь', eight='восемь', nine='девять', ten='десять')


# @profile()
def num_translate_rc(num):
    if rc_values.num:
        return rc_values.num
    else:
        print('None')


print(num_translate_rc('zero'))
print(num_translate_rc('fifty'))

print(rc_values)
