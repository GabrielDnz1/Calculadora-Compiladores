from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Analise.as_view()),
]