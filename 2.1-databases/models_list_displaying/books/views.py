from django.shortcuts import render
from .models import Book
from django.http import Http404
from datetime import date


def books_view(request, pub_date=None):
    template = 'books/books_list.html'

    if pub_date is not None:
        # Если pub_date пришел как datetime, берем только дату
        if hasattr(pub_date, 'date'):
            pub_date = pub_date.date()

        # Получаем книги за дату
        books = Book.objects.filter(pub_date=pub_date).order_by('pub_date')

        if not books.exists():
            raise Http404("No books found for this date.")

        # Получаем все уникальные даты
        all_dates = Book.objects.values_list('pub_date', flat=True).distinct().order_by('pub_date')
        dates_list = list(all_dates)

        # Находим предыдущую и следующую дату
        prev_date = None
        next_date = None

        if pub_date in dates_list:
            index = dates_list.index(pub_date)
            if index > 0:
                prev_date = dates_list[index - 1]
            if index < len(dates_list) - 1:
                next_date = dates_list[index + 1]

        context = {
            'books': books,
            'pub_date': pub_date,
            'prev_date': prev_date,
            'next_date': next_date,
        }
    else:
        books = Book.objects.all().order_by('pub_date')
        context = {
            'books': books,
            'pub_date': None,
            'prev_date': None,
            'next_date': None,
        }

    return render(request, template, context)