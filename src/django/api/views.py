from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import ResolvePost
from .serializers import ResolvePostSerializer
from .compilador import core

# Create your views here.
class ResolveView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ResolvePost.objects.all()
    serializer_class = ResolvePostSerializer
    
    def list(self, request):
        queryset = ResolvePost.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(core.getResponse(serializer.data))
        else: 
            return Response(serializer.errors, status=400)