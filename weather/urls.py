
from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:id>', views.delete),
]
