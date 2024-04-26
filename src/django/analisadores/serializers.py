from rest_framework import serializers
from .models import ResolvePost

class ResolvePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolvePost
        fields = ['id', 'title', 'content']