"""ChainMap принимает любое количество сопоставлений или
 словарей и превращать их в единое обновляемое представление."""
# парсинг + телеграм бот оповещение
from collections import ChainMap

computer_parts = {
    'system_bock': 1,
    'monitor': 1,
    'keyboard_mouse': 1
}

computer_options = {
    'RAM': '8 Gb',
    'HDD': '1000 Gb',
    'PROC': 'Intel Core i5'
}

computer_accessories = {
    'RAM': '6 Gb',
    'gaming': False,
    'divided': True,
}

lst = [computer_parts, computer_options, computer_accessories]
lst[0]['monitor']



"""
мы создали три словаря Python. 
Далее, мы создали экземпляр ChainMap, 
передав эти три словаря. В конце мы попытались 
получить доступ к одному из ключей в нашем ChainMap.
После этого, ChainMap пройдет через каждое сопоставление, 
чтобы увидеть, существует ли данный ключ и имеет ли он значение. 
Если это так, тогда ChainMap вернет первое найденное значение, 
которое соответствует ключу."""

computer_pricing = ChainMap(computer_options, computer_parts, computer_accessories)

print(computer_pricing)
# lst[0]['monitor']
print(computer_pricing['RAM'])

computer_pricing['opt'] = '20 Gb'

computer_pricing['RAM'] = '1000 Gb'
print(computer_options)
