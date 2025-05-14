from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings  # Добавьте этот импорт
from .forms import VacancyForm
from .models import NewsModel, ProductModel, VacancyModel, TypeProductModel


def home_page(request):
    return render(request, 'coffee_maf/main.html')


def news_list(request):
    news = NewsModel.objects.all().order_by('-id')
    return render(request, 'coffee_maf/news.html', {'news': news})


def products_list(request):
    product_types = TypeProductModel.objects.all()
    selected_type_id = request.GET.get('type')
    products = ProductModel.objects.all()

    if selected_type_id:
        products = products.filter(type_product_id=selected_type_id)

    return render(request, 'coffee_maf/products.html', {
        'products': products,
        'product_types': product_types,
        'selected_type_id': int(selected_type_id) if selected_type_id else None
    })


def vacancies_list(request):
    vacancies = VacancyModel.objects.all()

    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()

            email = EmailMessage(
                f'Новый отклик на вакансию: {candidate.vacancy.title}',
                f'''
                Имя: {candidate.name}
                Телефон: {candidate.phone}
                Email: {candidate.email}
                Вакансия: {candidate.vacancy.title}
                ''',
                settings.DEFAULT_FROM_EMAIL,
                ['m.rita1012@mail.ru'],
            )

            if candidate.resume:
                email.attach(candidate.resume.name, candidate.resume.read())

            try:
                email.send()
                print("Письмо отправлено!")
            except Exception as e:
                print(f"Ошибка отправки: {e}")

            return redirect('vacanse')
    else:
        form = VacancyForm()

    return render(request, 'coffee_maf/vacanse.html', {
        'vacancies': vacancies,
        'form': form
    })


def contacts_page(request):
    return render(request, 'coffee_maf/contacts.html')

def politic_page(request):
    return render(request, 'coffee_maf/politic.html')

def personalDate_page(request):
    return render(request, 'coffee_maf/personalDate.html')