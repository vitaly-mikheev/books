from django.db import models
# Create your models here.

class Book(models.Model):
    writer = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    price_in_cents = models.IntegerField()

    def __str__(self):
        return self.name
