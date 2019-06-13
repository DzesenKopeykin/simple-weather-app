from django.urls import path
from . import views


app_name = 'weather'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('remove_city/', views.remove_city, name='remove_city'),
]
