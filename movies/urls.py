from django.urls import path
from . import views

# here we map url endpoints to view functions
urlpatterns = [
    path("", views.index, name="movies_index"), # notice we are not calling it here
    path("<int:movie_id>", views.detail, name="movies_detail") # the "int:" limit the pattern to be int only
]