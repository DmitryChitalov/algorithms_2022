import hashlib

word = str(input("Enter your word: "))

a = set()
b = []

for i in range(len(word)):
    for l in range(len(word) - i + 1):
        if hashlib.sha256(word[l:l + i].encode()).hexdigest() not in a and word[l:l + i] != '':
            a.add(hashlib.sha256(word[l:l + i].encode()).hexdigest())
            b.append(word[l:l + i])

print(*b, sep='\n')