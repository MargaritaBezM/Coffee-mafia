from django.contrib import admin

from coffee_maf.models import *
from django.contrib.admin import AdminSite

AdminSite.site_header = "Кофе Мафия - Администрирование"
AdminSite.site_title = "Кофе Мафия"
AdminSite.index_title = "Панель управления"

NewsModel._meta.verbose_name = "Новость"
NewsModel._meta.verbose_name_plural = "Новости"

TypeProductModel._meta.verbose_name = "Тип товара"
TypeProductModel._meta.verbose_name_plural = "Типы товаров"

ProductModel._meta.verbose_name = "Товар"
ProductModel._meta.verbose_name_plural = "Товары"

VacancyModel._meta.verbose_name = "Вакансия"
VacancyModel._meta.verbose_name_plural = "Вакансии"

VacancyPersonModel._meta.verbose_name = "Отклик"
VacancyPersonModel._meta.verbose_name_plural = "Отклики"

admin.site.register(NewsModel)
admin.site.register(TypeProductModel)
admin.site.register(ProductModel)
admin.site.register(VacancyModel)
admin.site.register(VacancyPersonModel)

