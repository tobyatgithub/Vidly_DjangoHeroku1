from django.urls import path
from . import views

app_name = 'movies' # app_name is a reserved variable for django to recognize namespace pattern for url.
# here we map url endpoints to view functions
urlpatterns = [
    path("", views.index, name="index"), # notice we are not calling it here
    path("<int:movie_id>", views.detail, name="detail") # the "int:" limit the pattern to be int only
]