# Выходит не совсем верный ответ... Во множество попадает и слово целиком, и пустая подстрока (откуда?)

from hashlib import sha256

word = 'papa'
hash_set = set()

for i in range(len(word)):
    for j in range(i, len(word)+1):
        # print(word[i:j])
        hashed_element = sha256(word[i:j].encode()).hexdigest()
        hash_set.add(hashed_element)

print(f'Количество уникальных подстрок в слове {word}: {len(hash_set)}')
