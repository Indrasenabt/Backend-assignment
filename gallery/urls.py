from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteImageViewSet, RandomDogView, BreedDogView

router = DefaultRouter()
router.register(r'favorites', FavoriteImageViewSet, basename='favorite')

urlpatterns = [
    path('dogs/random/', RandomDogView.as_view(), name='random_dog'),
    path('dogs/breed/<str:breed>/', BreedDogView.as_view(), name='breed_dog'),
    path('', include(router.urls)),
]
