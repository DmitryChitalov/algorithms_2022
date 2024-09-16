from django.core.management import BaseCommand
from mainapp.models import Product, Category
# from django.contrib.auth.forms import User
# from authapp.forms import CustomUser, ShopUser
from django.template.defaultfilters import slugify
from unidecode import unidecode


import json, os

JSON_PATH = 'mainapp'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):

        categories = load_from_json('categories')

        Category.objects.all().delete()
        for category in categories:
            # print(category)
            category['slug'] = slugify(unidecode(category['name']))
            new_category = Category(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = Category.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            product['slug'] = slugify(unidecode(product['name']))
            new_product = Product(**product)
            new_product.save()


        # CustomUser.objects.create_superuser(
        #     'mikhail', 'tet@fds.rk', 'root' ,age = 20
        # )

        # ShopUser.objects.create_user(
        #     'mikhdfail', 'tet@fds.rk', 'royot', age=20
        # )