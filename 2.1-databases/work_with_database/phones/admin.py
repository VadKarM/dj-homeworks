from django.contrib import admin
from .models import Phone

# Регистрируем модель Phone в админке
admin.site.register(Phone)
