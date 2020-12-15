from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Movie

# if see pylint complain:  pip install pylint-django 
def index(request):
    movies = Movie.objects.all()
    # we pass data throught context arg
    return render(request, 'movies/index.html', context={'movies': movies}) 

def detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'movies/detail.html', context={'movie': movie})
    except Movie.DoesNotExist:
        raise Http404()

