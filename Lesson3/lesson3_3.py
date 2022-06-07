import hashlib

input_string = input("Введите строку: ")
substrings = []
my_lst = []
my_set = ()
for i in range(0, len(input_string) + 1):
    for j in range(i + 1, len(input_string) + 1):
        my_word = hashlib.md5(input_string.encode()).hexdigest()
        substr = hashlib.md5(input_string[i:j].encode()).hexdigest()
        substrings.append(substr)
        my_set = set(substrings)
        my_set.discard(my_word)
        word_string = input_string[i:j]

print(f'{len(my_set)} уникальных подстрок')
