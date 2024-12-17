"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import uuid


class WebCache:
    def __init__(self):
        self.cache = {}

    # Функция для генерации уникального идентификатора для url
    def generate_uuid(self, url):
        # Генерация уникального идентификатора для url с использованием uuid4
        return uuid.uuid4().hex

    # Функция для получения UUID из кэша или генерации нового
    def get_cache(self, url):
        cache_url = self.cache.get(url)
        if cache_url:
            # Если URL уже есть в кэше, возвращаем UUID
            return cache_url

        # Если URL нет в кэше, генерируем новый UUID
        new_uuid = self.generate_uuid(url)
        # Сохраняем в кэш
        self.cache[url] = new_uuid
        return new_uuid


# Пример использования
if __name__ == "__main__":
    web_cache = WebCache()

    # Пример с двумя URL-адресами
    url_1 = "https://example.com/page1"
    url_2 = "https://example.com/page2"

    # Получаем UUID для первого URL
    print("UUID для страницы 1:", web_cache.get_cache(url_1))

    # Получаем UUID для второго URL
    print("UUID для страницы 2:", web_cache.get_cache(url_2))

    # Повторно получаем UUID для первого URL
    print("Повторный UUID для страницы 1:", web_cache.get_cache(url_1))
