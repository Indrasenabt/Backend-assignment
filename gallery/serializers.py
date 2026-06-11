from rest_framework import serializers
from .models import FavoriteImage

class FavoriteImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FavoriteImage
        fields = ('id', 'user', 'image_url', 'breed', 'notes', 'tags', 'created_at')
        read_only_fields = ('id', 'created_at', 'user')

class FavoriteImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteImage
        fields = ('notes', 'tags')
