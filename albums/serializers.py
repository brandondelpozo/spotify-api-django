from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Album