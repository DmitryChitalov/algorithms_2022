"""Примеры с sha"""

import hashlib


# -------------------------------------sha1-----------------------------------#
hash_obj = hashlib.sha1(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()

print(hex_dig_res)  # -> d9536c477c646977dce73445a656a9c5e1c19d59

print()

# ------------------------------------sha224----------------------------------#
hash_obj = hashlib.sha224(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
                # -> 5a39dff4807dc145be2cc85efa7b4c165bed383e69e0691546b2589f

print(hex_dig_res)

print()

# ------------------------------------sha256----------------------------------#
hash_obj = hashlib.sha256(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
        # -> c54034d262f7c0b9b82ce4988f115925ee684dd39e399c9ddea0c776d27d7521

print(hex_dig_res)

print()

# -----------------------------------sha384-----------------------------------#
hash_obj = hashlib.sha384(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
# -> 4080aa6d42e2a67c1f6307771ecbe11a23ec8283fd775d72
# 0381844cb3b9e4d038f5446f9db3123bbb4bba588c436f3f

print(hex_dig_res)

print()

# ----------------------------------sha512------------------------------------#
hash_obj = hashlib.sha512(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
# -> d4ea479e7b84b3c71416311af2e79f2919233775f86a8273eaf7e14440a
# 306df6ad9587a1d6fe624529118efa2b55740a138276a0630dc0b059066ddaec7a60f

print(type(hex_dig_res))
