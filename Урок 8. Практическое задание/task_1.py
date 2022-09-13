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


class HuffmanCode:
    def __init__(self, probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if (value >= self.probability[j]):
                return j
        return index - 1

    def compute_code(self):
        num = len(self.probability)
        huffman_code = [''] * num

        for i in range(num - 2):
            val = self.probability[num - i - 1] + self.probability[num - i - 2]
            if (huffman_code[num - i - 1] != '' and huffman_code[num - i - 2] != ''):
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif (huffman_code[num - i - 1] != ''):
                huffman_code[num - i - 2] = '0'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif (huffman_code[num - i - 2] != ''):
                huffman_code[num - i - 1] = '1'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:
                huffman_code[num - i - 1] = '1'
                huffman_code[num - i - 2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if (isinstance(huffman_code[num - i - 2], list) and isinstance(huffman_code[num - i - 1], list)):
                complete_code = huffman_code[num - i - 1] + huffman_code[num - i - 2]
            elif (isinstance(huffman_code[num - i - 2], list)):
                complete_code = huffman_code[num - i - 2] + [huffman_code[num - i - 1]]
            elif (isinstance(huffman_code[num - i - 1], list)):
                complete_code = huffman_code[num - i - 1] + [huffman_code[num - i - 2]]
            else:
                complete_code = [huffman_code[num - i - 2], huffman_code[num - i - 1]]

            huffman_code = huffman_code[0:(len(huffman_code) - 2)]
            huffman_code.insert(position, complete_code)

        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        if (len(huffman_code[1]) == 0):
            huffman_code[1] = '1'

        count = 0
        final_code = [''] * num

        for i in range(2):
            for j in range(len(huffman_code[i])):
                final_code[count] = huffman_code[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code


string = input('Введите строку для кодирования: ')

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
length = len(string)

probabilities = [float("{:.2f}".format(frequency[1] / length)) for frequency in freq]
probabilities = sorted(probabilities, reverse=True)

huffmanClassObject = HuffmanCode(probabilities)
P = probabilities

huffman_code = huffmanClassObject.compute_code()

for id, char in enumerate(freq):
    if huffman_code[id] == '':
        print(char[0], 1)
        continue
    print(char[0], huffman_code[id])
