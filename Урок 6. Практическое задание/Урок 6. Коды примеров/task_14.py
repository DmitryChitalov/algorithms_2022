from json import loads, dumps
from pympler import asizeof

gen_dict = {i: i * 2 for i in range(100000)}
dumped_dict = dumps(gen_dict)
print(type(dumped_dict))

out_dict = loads(dumped_dict)
print(type(out_dict))

print('Размер dict: ', asizeof.asizeof(gen_dict))
print('Размер json: ', asizeof.asizeof(dumped_dict))

"""
<class 'dict'>
<class 'str'>
Размер dict:  11638840
Размер json:  1633384
"""
