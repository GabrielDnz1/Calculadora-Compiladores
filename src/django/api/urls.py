from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('backend', views.ResolveView, basename='backend')

urlpatterns = router.urls