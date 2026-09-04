import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    # Метод handle — это основная логика команды.
    def handle(self, *args, **options):
        # Удаляем старые данные, чтобы избежать ошибок с дубликатами (например, если команда запускалась ранее)
        Phone.objects.all().delete()

        # Открываем CSV-файл. Важно указать кодировку 'utf-8', иначе кириллица может "сломаться".
        with open('phones.csv', 'r', encoding='utf-8') as file:
            # Используем csv.DictReader, чтобы работать с данными, обращаясь к ним по названию столбцов (id, name...)
            # delimiter=';' указывает, что в файле поля разделены точкой с запятой.
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            # Создаем объект модели Phone
            phone = Phone(
                # Преобразуем данные из CSV в нужные типы Python
                id=int(phone_data['id']),
                name=phone_data['name'],
                image=phone_data['image'],
                price=float(phone_data['price']),
                release_date=phone_data['release_date'],
                lte_exists=phone_data['lte_exists'] == 'True',
                # Генерируем slug из названия, превращая "Samsung Galaxy Edge 2" в "samsung-galaxy-edge-2"
                slug=slugify(phone_data['name'])
            )
            # Сохраняем объект в базу данных
            phone.save()

        # Выводим сообщение об успешном завершении
        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))