"""Так делать плохо?"""

md5(sha1(password))
md5(md5(salt) + md5(password))
sha1(sha1(password))
sha1(str_rot13(password + salt))
md5(sha1(md5(md5(password) + sha1(password)) + md5(password)))

# поэтому лучше просто "солить" хеши
# sha256 + соль