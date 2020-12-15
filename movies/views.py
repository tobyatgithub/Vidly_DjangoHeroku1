from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# if see pylint complain:  pip install pylint-django 
def index(request):
    movies = Movie.objects.all()
    # we pass data throught context arg
    return render(request, 'movies/index.html', context={'movies': movies}) 

def detail(request, movie_id):
    return HttpResponse(movie_id)
