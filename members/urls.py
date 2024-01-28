from django.urls import path
from . import views

urlpatterns = [
    # path('', views.members, name='members'),
    path('members/', views.members, name='members'), #siempre irá el nombre de la app
    path('members/details/<int:id>', views.details, name='details'),
]
