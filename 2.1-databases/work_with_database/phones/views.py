from django.shortcuts import render, get_object_or_404, redirect
from .models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort_by = request.GET.get('sort', 'name')

    if sort_by == 'min_price':
        order_by = 'price'
    elif sort_by == 'max_price':
        order_by = '-price'
    else:  # default 'name'
        order_by = 'name'

    phones = Phone.objects.all().order_by(order_by)

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)

    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)