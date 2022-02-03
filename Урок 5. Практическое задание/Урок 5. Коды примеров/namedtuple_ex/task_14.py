"""Класс collections.namedtuple()"""

from collections import namedtuple

# 'Resume' - имя кортежа
# создаем шаблон кортежа
RES = namedtuple('Resume', 'id first_name second_name')
print(RES)  # -> <class '__main__.Resume'>
# заполняем шаблон данными
RESUME_PARTS = RES(
    id=1,
    first_name='Ivan',
    second_name='Ivanov'
)

RESUME_PARTS = RES(
    id=1,
    first_name='Ivan',
    second_name='Ivanov'
)

RESUME_PARTS = RES(
    id=1,
    first_name='Ivan',
    second_name='Ivanov'
)

print(RESUME_PARTS)
print(RESUME_PARTS[0])  # -> Resume(id='1', first_name='Ivan',
                                                    # second_name='Ivanov')
"""
1) меньше памяти
2) по скорости
"""

(1, 2, 3, 4, 5, 6, 7, 8)

# списки быстрее

# recordclass