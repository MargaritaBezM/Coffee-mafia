from django.urls import path
from . import views
from django.conf.urls import handler404
from coffee_maf.views import notFound_page

handler404 = notFound_page

urlpatterns = [
    path('', views.home_page, name='main'),
    path('news.html/', views.news_list, name='news'),
    path('products.html/', views.products_list, name='products'),
    path('vacanse.html/', views.vacancies_list, name='vacanse'),
    path('contacts.html/', views.contacts_page, name='contacts'),
    path('politic.html/', views.politic_page, name='politic'),
    path('personalDate.html/', views.personalDate_page, name='personalDate'),

]
