from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('<int:receita_id>', views.receita, name='receita')
]