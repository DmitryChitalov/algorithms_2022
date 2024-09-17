import hashlib

hash_mnozestvo = set() # множество для хэшей
string = input(": ")
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        print(string[i:j])
        hash_mnozestvo.add(hashlib.sha256(string[i:j].encode()).hexdigest())

print(hash_mnozestvo)