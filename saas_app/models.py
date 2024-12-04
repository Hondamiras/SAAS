from django.db import models
from django.urls import reverse
from datetime import datetime

class AboutUs(models.Model):
    image = models.ImageField(upload_to='about_us/', verbose_name='Изображение')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Facility(models.Model):
    image = models.ImageField(upload_to='facilities/', verbose_name='Изображение')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse('facility_detail', kwargs={'facility_slug': self.slug})

class News(models.Model):
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='Изображение')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class KnittedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Category.Status.KNITTED)

class FabricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Category.Status.FABRIC)

class Category(models.Model):
    class Status(models.TextChoices):
        KNITTED = 'KN', 'Knitted'
        FABRIC = 'FAB', 'Fabric'

    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение')
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.KNITTED, verbose_name='Тип материала')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_products', kwargs={'category_slug': self.slug})

    objects = models.Manager()
    knitted = KnittedManager()
    fabric = FabricManager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='Продукт')
    image = models.ImageField(upload_to='product_images/', verbose_name='Дополнительное изображение')

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = 'Фото Продукта'
        verbose_name_plural = 'Фото Продуктов'
