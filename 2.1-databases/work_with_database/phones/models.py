from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # Django автоматически создает поле id, которое является primary_key.
    # Но задание требует явно указать, что id — это основной ключ. Это просто для ясности.
    id = models.IntegerField(primary_key=True)

    # Поле для названия телефона
    name = models.CharField(max_length=100)

    # URL для изображения. URLField — это поле для ссылок
    image = models.URLField()

    # Цена. DecimalField лучше, чем FloatField, для работы с деньгами (точность)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Дата выпуска
    release_date = models.DateField()

    # Логическое поле: есть LTE или нет
    lte_exists = models.BooleanField()

    # Slug — это часть URL-адреса, удобная для человека, например, 'iphone-x'.
    # Он должен быть уникальным, чтобы можно было найти конкретную запись.
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name