import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def get_bus_stations():
    """Читает CSV-файл и возвращает список словарей"""
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def bus_stations(request):
    # Получаем все остановки из CSV
    all_stations = get_bus_stations()

    # Создаем пагинатор (10 записей на страницу)
    paginator = Paginator(all_stations, 10)

    # Получаем номер страницы из GET-параметров
    page_number = request.GET.get('page', 1)

    # Получаем объект страницы
    page = paginator.get_page(page_number)

    # Формируем контекст для шаблона
    context = {
        'bus_stations': page.object_list,  # Список остановок на странице
        'page': page,  # Объект страницы
    }

    return render(request, 'stations/index.html', context)