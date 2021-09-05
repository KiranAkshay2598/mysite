from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home_view, name='home_url'),
    path('add',views.add, name='add_url')
]