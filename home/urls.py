from django.urls import path
from .views import index

app_name= "home"

urlpatterns=[
    path("index", index, name="home-index")
]