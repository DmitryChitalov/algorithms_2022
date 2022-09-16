# Это файл для пятого скрипта

from pympler import asizeof
from numpy import array
# курс основ дз5 задание 3
# оптимизированная
tutors = array(['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'])
classes = array(['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'])


def check_gen(teachers, clas):
    i = 0
    j = 0
    while i != len(clas):
        if j == clas[-1]:
            yield (None, clas[j])
            i += 1
            j += 1
        elif i == teachers[-1]:
            yield (teachers[i], None)
        else:
            yield (teachers[i], clas[j])
            i += 1
            j += 1
    return 0


generator = check_gen(tutors, classes)
for _ in range(len(tutors)):
    print(next(generator))

print(asizeof.asizeof(check_gen(tutors, classes)))
# 1048

# неоптимизиррованная
tutors_2 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes_2 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen_2(teachers, clas):
    i = 0
    j = 0
    while i != len(clas):
        if j == clas[-1]:
            yield (None, clas[j])
            i += 1
            j += 1
        elif i == teachers[-1]:
            yield (teachers[i], None)
        else:
            yield (teachers[i], clas[j])
            i += 1
            j += 1
    return 0


generator = check_gen_2(tutors, classes)
for _ in range(len(tutors)):
    print(next(generator))


print(asizeof.asizeof(check_gen_2(tutors_2, classes_2)))
# 1880

# Использование array из библиотеки numpy сократило использование памяти почти в 2 раза