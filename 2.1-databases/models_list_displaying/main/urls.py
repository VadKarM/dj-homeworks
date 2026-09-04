from django.contrib import admin
from django.urls import path, register_converter
from books.views import books_view
from books.converters import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
    path('books/', books_view, name='books'),
    path('books/<date:pub_date>/', books_view, name='books_by_date'),  # ← ОБРАТИ ВНИМАНИЕ!
    path('admin/', admin.site.urls),
]