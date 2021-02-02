from django.urls import path
from . import views


urlpatterns = [
    path("cars/", views.cars, name="cars"),
    path("popular/", views.rating, name="rating"),
    path("rate/<int:pk>/", views.car, name="car"),
    # template url
    # path("", views.api_search, name="home"),
]