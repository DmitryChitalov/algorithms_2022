"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


def get_unique_substrings(str_obj: str) -> int:
    unique_hashes = set()
    N = len(str_obj)
    # Перебираем все возможные подстроки
    for i in range(N):
        for j in range(i + 1, N + 1):
            substring = str_obj[i:j]
            # Проверяем является ли это подстрокой
            if substring != str_obj:
                # Вычисляем хеш подстроки (используем hashlib для надежного хеширования)
                hash_value = hashlib.sha256(substring.encode('utf-8')).hexdigest()
                if hash_value not in unique_hashes:
                    print(substring)
                    unique_hashes.add(hash_value)
    return len(unique_hashes)


# Пример использования
str_obj = "рара"
print(f"{str_obj} - {get_unique_substrings(str_obj)}  уникальных подстрок")
