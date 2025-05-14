from django.db import models
from django.utils import timezone

class NewsModel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField(upload_to='news_images')
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f"{self.title}"

class TypeProductModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"

class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='product_images')
    price = models.IntegerField()
    description = models.TextField(max_length=1000, null=False, blank=False)
    volume = models.TextField(max_length=100, null=True, blank=False)
    type_product = models.ForeignKey(TypeProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class VacancyModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='vacancy_images')

    def __str__(self):
        return f"{self.title}"

class VacancyPersonModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    vacancy = models.ForeignKey('VacancyModel', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume/', verbose_name="Резюме")
    created_at = models.DateTimeField(default=timezone.now)
    position_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name}"