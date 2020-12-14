from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_len=255)

class Movie(models.Model):
    title = models.CharField(max_len=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = model.FloatField()
    genre = model.ForeignKey(Genre, on_delete=model.CASCADING)
    # cacading = if a genre is deleted, than all movies with same genre will be deleted.
