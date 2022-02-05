from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    is_valid = models.BooleanField(default=True, verbose_name="Доступен")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name='products', verbose_name="Категория",db_index=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(unidecode(self.name))
        super(Product, self).save()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:details',
                       args=[self.slug])