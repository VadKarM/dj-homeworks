import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def handle(self, *args, **options):
        Phone.objects.all().delete()

        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            phone = Phone(
                id=int(phone_data['id']),
                name=phone_data['name'],
                image=phone_data['image'],
                price=float(phone_data['price']),
                release_date=phone_data['release_date'],
                lte_exists=phone_data['lte_exists'] == 'True',
                slug=slugify(phone_data['name'])
            )
            phone.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))