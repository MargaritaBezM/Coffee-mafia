from django.contrib import admin

from coffee_maf.models import *
from django.contrib.admin import AdminSite

AdminSite.site_header = "Кофе Мафия - Администрирование"
AdminSite.site_title = "Кофе Мафия"
AdminSite.index_title = "Панель управления"


admin.site.register(NewsModel, verbose_name="Новость", verbose_name_plural="Новости")
admin.site.register(TypeProductModel, verbose_name="Тип товара", verbose_name_plural="Типы товаров")
admin.site.register(ProductModel, verbose_name="Товар", verbose_name_plural="Товары")
admin.site.register(VacancyModel, verbose_name="Вакансия", verbose_name_plural="Вакансии")
admin.site.register(VacancyPersonModel, verbose_name="Отклик", verbose_name_plural="Отклики")

