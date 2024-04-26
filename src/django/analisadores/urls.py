from django.urls import path
from . import views 

urlpatterns = [
    path('api/resolve/', views.ResolveView.as_view(), name='resolve'),
]