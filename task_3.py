from hashlib import sha256

st = str(input('Введите строку: '))
res = set()

for i in range(len(st)):
    for j in range(i + 1, len(st) + 1):
        if st[i:j] != st:
            un = st[i:j]
            print(un)
            res.add(sha256(un.encode()).hexdigest())

print(res)
print(f'Уникальных подстрок: {len(res)}')