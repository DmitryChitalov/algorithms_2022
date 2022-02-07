"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
# ====== Итоговый вывод ========
# message = 'beep boop beer!'
# message_code = ['00', '11', '11', '011', '101', '00', '010', '010', '011', '101', '00', '11', '11', '1001', '1000']
# ==============================
# code_table:
# {' ': '101',
#  '!': '1000',
#  'b': '00',
#  'e': '11',
#  'o': '010',
#  'p': '011',
#  'r': '1001'}
# ==============================
# Sending message...
# Receiving message...
# Get message: beep boop beer!

from collections import Counter
from dataclasses import dataclass
from pprint import pprint
import shelve


class HuffmanCoding:
    @dataclass
    class Element:
        name: str
        weight: int
        tree: dict()

    @classmethod
    def get_huffman_code(cls, message: str):
        elements_frequency = cls.get_elements_frequency(message)
        tree = cls.get_huffman_tree(elements_frequency)
        code_table = cls.get_huffman_table(tree)
        code = []
        for letter in message:
            code.append(code_table[letter])
        return code, code_table

    @classmethod
    def get_elements_frequency(cls,message: str):
        element_frequency = sorted(Counter(message).items(), 
                                    key=lambda el: (el[1], el[0]), 
                                    reverse=True)

        element_frequency = [cls.Element(name=element, weight=weight, tree=element) 
                            for element, weight in element_frequency]
        return element_frequency

    @classmethod
    def get_huffman_tree(cls, element_frequency: list[Element]):
        if len(element_frequency) == 0:
            return {}
        elif len(element_frequency) == 1:
            return {0: element_frequency.pop().name}
            
        while len(element_frequency) >= 2:
            first_element_frequency = element_frequency.pop()
            second_element_frequency = element_frequency.pop()

            new_name = (f'{first_element_frequency.name}'
                        f'{second_element_frequency.name}')

            new_weight = (first_element_frequency.weight + 
                                                    second_element_frequency.weight)
            tree = {0: first_element_frequency.tree, 
                    1: second_element_frequency.tree}
            new_element_frequency = cls.Element(new_name, new_weight, tree)
            if not element_frequency:
                break
                
            if new_weight <= element_frequency[-1].weight:
                element_frequency.append(new_element_frequency)
            elif new_weight > element_frequency[0].weight:
                element_frequency.insert(0, new_element_frequency)
            else: 
                for i in range(-1, -len(element_frequency)-1, -1):
                    cur_element = element_frequency[i]
                    if new_weight <= cur_element.weight:
                        element_frequency.insert(i+1, new_element_frequency)
                        break
        
        return new_element_frequency.tree  

    @classmethod
    def get_huffman_table(cls, tree: dict):
        code_table = {}
        def fill_code_table(tree, path=''):
            if not isinstance(tree, dict):
                code_table[tree] = path
            elif len(tree) == 1:
                fill_code_table(tree[0], path=f'{path}0')
            else:
                fill_code_table(tree[0], path=f'{path}0')
                fill_code_table(tree[1], path=f'{path}1')

        fill_code_table(tree, path='')

        return code_table
      

class Sender:
    @staticmethod
    def send_message(message_code, *, setter, **kwargs):
        with shelve.open('resourse') as db:
            db['message_code'] = message_code
            db['code_table'] = kwargs['code_table']


class Recipient:
    @classmethod
    def get_message(cls, *, getter, resourse):
        with shelve.open('resourse') as db:
            message_code = db['message_code']
            code_table = db['code_table']
            return cls.decode_huffman_message(message_code, code_table)
    
    @classmethod
    def decode_huffman_message(cls, message_code: list, code_table: dict):
        message = []
        for cur_code in message_code:
            for letter, code in code_table.items():
                if cur_code == code:
                    message.append(letter)
                    break          
        return ''.join(message)


        

message = 'beep boop beer!'
message_code, code_table = HuffmanCoding.get_huffman_code(message)
print(f'{message_code = }')
print('='*30)
print('code_table: ')
pprint(code_table)
print('='*30)
print('Sending message...')
Sender.send_message(message_code, 
                    setter=shelve.open, 
                    resourse='resourse', 
                    code_table=code_table)
print('Receiving message...')
message = Recipient.get_message(getter=shelve.open, resourse='resourse')
print(f'Get message: {message}')





