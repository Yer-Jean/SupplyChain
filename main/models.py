from django.db import models

from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    model = models.CharField(max_length=100, verbose_name='Модель', **settings.NULLABLE)
    launch_date = models.DateField(verbose_name='Дата старта продаж')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class SupplyNode(models.Model):
    CATEGORY_CHOICES = (
        ('FCT', 'Factory'),
        ('RET', 'Retail'),
        ('ENT', 'Entrepreneur')
    )
    name = models.CharField(max_length=100, verbose_name='Наименование')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3, verbose_name='Категория')
    supplier_tier = models.ForeignKey('self', on_delete=models.CASCADE,
                                      verbose_name='Поставщик', **settings.NULLABLE)
    products = models.ManyToManyField(Product, verbose_name='Товары')
    debt = models.DecimalField(default=0, max_digits=10, decimal_places=2,
                               verbose_name='Задолженность', **settings.NULLABLE)
    tier = models.PositiveSmallIntegerField(default=0, verbose_name='Уровень поставщика')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name} - {self.get_category_display()}'

    class Meta:
        verbose_name = 'Торговое звено'
        verbose_name_plural = 'Торговые звенья'


class Contact(models.Model):
    supply_node = models.ForeignKey(SupplyNode, on_delete=models.CASCADE, verbose_name='Наименование')
    email = models.EmailField(verbose_name='Email', **settings.NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город', **settings.NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **settings.NULLABLE)
    building_number = models.CharField(max_length=50, verbose_name='Номер дома', **settings.NULLABLE)

    def __str__(self):
        return f'{self.supply_node.name} - {self.country}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
