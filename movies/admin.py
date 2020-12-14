from django.contrib import admin
from .models import Movie, Genre
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_in_stock', 'daily_rate')
    # to hide the date_created field from the admin add movie page
    exclude = ('date_created',) 

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

