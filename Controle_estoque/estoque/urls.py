from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:quantidade>", views.qtd, name='quantidade')
]