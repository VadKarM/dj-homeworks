from django.shortcuts import render, get_object_or_404, redirect
from .models import Phone

def index(request):
    # При заходе на главную страницу перенаправляем пользователя на каталог
    return redirect('catalog')

def show_catalog(request):
    # Получаем параметр сортировки из URL. Если параметра 'sort' нет, сортируем по имени по умолчанию.
    sort_by = request.GET.get('sort', 'name')

    # Определяем, по какому полю и в каком порядке сортировать
    if sort_by == 'min_price':
        order_by = 'price'
    elif sort_by == 'max_price':
        order_by = '-price'  # Знак '-' означает сортировку по убыванию
    else:  # default 'name'
        order_by = 'name'

    # Получаем все телефоны из базы данных, отсортированные нужным образом
    phones = Phone.objects.all().order_by(order_by)

    # Передаем данные в шаблон 'catalog.html'
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    # Находим телефон по слгу. Если его нет, автоматически возвращается ошибка 404.
    phone = get_object_or_404(Phone, slug=slug)

    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)