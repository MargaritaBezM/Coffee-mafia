from django.contrib import admin

from coffee_maf.models import *
from django.contrib.admin import AdminSite

AdminSite.site_header = "Кофе Мафия - Администрирование"
AdminSite.site_title = "Кофе Мафия"
AdminSite.index_title = "Панель управления"


# Register your models here.
admin.site.register(NewsModel)
admin.site.register(TypeProductModel)
admin.site.register(ProductModel)
admin.site.register(VacancyModel)
admin.site.register(VacancyPersonModel)

