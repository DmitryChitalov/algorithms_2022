import hashlib
import uuid

book = {}

def cash(url):
    global book
    if url in book.keys():
        return print(book.get(url))
    else:
        salt = uuid.uuid4().bytes
        return book.setdefault(url, hashlib.sha256(salt + url.encode()).hexdigest())


cash('A')
cash('A')
cash('B')
cash('A')
cash('B')