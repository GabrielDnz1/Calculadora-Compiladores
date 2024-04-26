from rest_framework import generics
from .models import ResolvePost
from .serializers import ResolvePostSerializer
from .classes import lexico

# Create your views here.
class ResolveView(generics.ListCreateAPIView):
    queryset = ResolvePost.objects.all()
    serializer_class = ResolvePostSerializer
    