from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all() # lazy loading, only returns a query
        resource_name = 'movies' # ...website/api/<resource_name>
        excludes = ['date_created'] # hide attributes
