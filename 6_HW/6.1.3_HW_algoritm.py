# птимизировал часть кода 3 урока задания 1. хранение в словаре сделал сериализацию. Экономии памяти в 3.5 раза
from json import loads, dumps
from pympler import asizeof

dict_num = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
            }

# 1784
print(asizeof.asizeof(dict_num))

dump_dict_num = dumps(dict_num)

# 456
print(asizeof.asizeof(dump_dict_num))