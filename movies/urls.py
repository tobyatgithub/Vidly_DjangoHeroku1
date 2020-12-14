from django.urls import path
from . import views

# here we map url endpoints to view functions
urlpatterns = [
    path("", views.index, name="index"), # notice we are not calling it here
]