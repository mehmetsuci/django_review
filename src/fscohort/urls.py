from django.urls import path
from .views import home_view, about

urlpatterns = [
    path("home/", home_view),
    path("about/", about)
]
