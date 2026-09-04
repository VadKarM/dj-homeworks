from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)

    image = models.URLField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    release_date = models.DateField()

    lte_exists = models.BooleanField()

    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name