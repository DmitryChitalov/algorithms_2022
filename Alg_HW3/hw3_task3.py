import hashlib


def return_hash_set(input_string):
    length = len(input_string)
    has_ob = set(hashlib.sha256(input_string[i:j + 1].encode()).hexdigest()
                 for i in range(length) for j in range(i, length))
    has_ob.remove(hashlib.sha256(input_string.encode()).hexdigest())
    res = set(input_string[i:j + 1] for i in range(length) for j in range(i, length)
              if hashlib.sha256(input_string[i:j + 1].encode()).hexdigest() in has_ob)
    return res, has_ob


result, set_for_hash = return_hash_set('rarap')
print("Подстроки. Число подстрок:", len(result), result)
print('Хэши', set_for_hash)
