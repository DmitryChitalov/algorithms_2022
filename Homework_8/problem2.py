class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

def calc_prob(file):
    symbols = dict()
    for el in file:
        if symbols.get(el) is None:
            symbols[el] = 1
        else:
            symbols[el] += 1
    return symbols

codes = dict()
def calc_codes(node, val=''):
    new_val = val + str(node.code)
    if node.left:
        calc_codes(node.left, new_val)
    if node.right:
        calc_codes(node.right, new_val)
    else:
        codes[node.symbol] = new_val
    return codes

def out_enc(file, coding):
    enc_out = []
    for c in file:
        print(coding[c], end='')
        enc_out.append(coding[c])

    string = ''.join([str(i) for i in enc_out])
    return string

def haffman_coding(file):
    symbol_with_probs = calc_prob(file)
    symbols = symbol_with_probs.keys()
    probs = symbol_with_probs.values()
    print('Symbols: ', symbols)
    print('Probs: ', probs)

    nodes = []
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1
        NewNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(NewNode)

    huffman_enc = calc_codes(nodes[0])
    print(huffman_enc)
    enc_out = out_enc(file, huffman_enc)
    print(enc_out)
    return
haffman_coding('ABCD')