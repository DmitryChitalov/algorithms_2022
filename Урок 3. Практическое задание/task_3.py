import hashlib

s_str = 'papa'
s_set = set()
for i in range(len(s_str)):
    for j in range(i+1, len(s_str)+1):
        if s_str[i:j] != s_str:
            s_set.add(hashlib.sha256(s_str[i:j].encode()).hexdigest())

print(f'В строке “{s_str}” {len(s_set)} уникальных подстрок')