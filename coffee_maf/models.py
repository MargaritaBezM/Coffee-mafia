from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField(upload_to='news_images')
    description = models.TextField(max_length=500, null=False, blank=False)


class TypeProductModel(models.Model):
    title = models.CharField(max_length=255)


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='product_images')
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField(max_length=500, null=False, blank=False)
    type_product = models.ForeignKey(TypeProductModel, on_delete=models.CASCADE)


class VacancyModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='vacancy_images')


class VacancyPeersonModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    vacancy = models.ForeignKey(VacancyModel, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume_document')
