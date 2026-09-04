from django.contrib import admin
from .models import Book

# Регистрируем модель Book для админки
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_date')  # Поля в списке
    list_filter = ('pub_date',)  # Фильтр по дате
    search_fields = ('name', 'author')  # Поиск
    ordering = ('pub_date',)  # Сортировка по дате