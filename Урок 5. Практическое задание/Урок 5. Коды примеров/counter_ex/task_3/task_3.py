# SEO
import re
from collections import Counter

find_words = re.findall(r'\w+', open('mtsuri.txt', encoding='utf-8').read())


def tf_calc(text):
    # преобразуем входной список в каунтер
    # показатель важности слова в контексте
    tf_text = Counter(text)
    # используем генератор словарей для деления значения каждого элемента
    # в каунтере на общее число слов в тексте - т.е. длину списка слов.
    tf_text = {i: tf_text[i] / len(text) for i in tf_text}
    return tf_text


print(tf_calc(find_words))  # -> {'Мой': 0.0003048780487804878,
# 'дядя': 0.0006097560975609756,
# 'самых': 0.0003048780487804878,
# 'честных': 0.0003048780487804878,
# 'правил': 0.0003048780487804878}
