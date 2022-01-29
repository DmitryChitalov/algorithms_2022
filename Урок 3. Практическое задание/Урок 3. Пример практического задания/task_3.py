import hashlib

some_set = set()  # создаем множество для хранения хешированныйх подстрок
some_str = 'papa'
for i in range(len(some_str)):
    for j in range(i + 1, len(some_str) + 1):
        if some_str[i:j] != some_str:  # исключаем запись слова целикм
                            # в множество, записываем только подстроки
            some_set.add(hashlib.sha256(some_str[i:j].encode()).hexdigest())
            print(some_str[i:j], end=' ')  # выводим для наглядности
                                # все возможные подстроки, включая дубли
print(f'\n{some_set}')  # выводим содержимое множества
print(f'Количество элементов в множестве: {len(some_set)}')
