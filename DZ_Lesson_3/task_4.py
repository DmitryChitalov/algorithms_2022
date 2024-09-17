import hashlib

ll = []

user = input("введите ссылку: ")

def hashirator(u):
    if hashlib.sha256(u.encode()).hexdigest() in ll:
        print("✅ В кэше есть такая ссылка")
    else:
        print("❌ Такой ссылки нет в кэше")
        ll.append(hashlib.sha256(u.encode()).hexdigest())

hashirator(user) # тут ссылки нет,
print(ll)
hashirator(user) # а тут ссылка уже есть
print(ll)