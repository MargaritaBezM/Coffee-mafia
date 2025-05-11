from django.shortcuts import render
from .models import NewsModel, ProductModel, VacancyModel
def home_page(request):
    return render(request, 'coffee_maf/main.html')

def news_list(request):
    news = NewsModel.objects.all().order_by('-id')
    return render(request, 'coffee_maf/news.html', {'news': news})

def products_list(request):
    products = ProductModel.objects.all()
    return render(request, 'coffee_maf/products.html', {'products': products})

def vacancies_list(request):
    vacancies = VacancyModel.objects.all()
    return render(request, 'coffee_maf/vacanse.html', {'vacancies': vacancies})

def contacts_page(request):
    return render(request, 'coffee_maf/contacts.html')