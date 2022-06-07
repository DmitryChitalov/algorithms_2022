from hashlib import sha256

word = 'papa'
hash_set = set()
str_set = set()

for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        # print(word[i:j])
        if word[i:j] != word:
            hashed_element = sha256(word[i:j].encode()).hexdigest()
            hash_set.add(hashed_element)
            # str_set.add(word[i:j])

print(f'Количество уникальных подстрок в слове {word}: {len(hash_set)}')
# print(str_set)
