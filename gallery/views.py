from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import FavoriteImage
from .serializers import FavoriteImageSerializer, FavoriteImageUpdateSerializer
from .services import DogAPIService

class RandomDogView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = DogAPIService.get_random_image()
        if data:
            return Response(data)
        return Response({"error": "Failed to fetch from Dog API"}, status=status.HTTP_502_BAD_GATEWAY)

class BreedDogView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, breed):
        data = DogAPIService.get_images_by_breed(breed)
        if data:
            return Response(data)
        return Response({"error": f"Failed to fetch images for breed: {breed}"}, status=status.HTTP_404_NOT_FOUND)

class FavoriteImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return FavoriteImage.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return FavoriteImageUpdateSerializer
        return FavoriteImageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

