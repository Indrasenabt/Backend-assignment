from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import FavoriteImage

class PetGalleryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)

    def test_fetch_random_dog(self):
        response = self.client.get('/api/dogs/random/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('image_url', response.data)

    def test_create_favorite(self):
        data = {
            "image_url": "https://images.dog.ceo/breeds/beagle/n02088364_10.jpg",
            "breed": "beagle",
            "notes": "Cute beagle",
            "tags": ["beagle", "cute"]
        }
        response = self.client.post('/api/favorites/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FavoriteImage.objects.count(), 1)
        self.assertEqual(FavoriteImage.objects.get().breed, 'beagle')

    def test_get_favorites(self):
        FavoriteImage.objects.create(
            user=self.user,
            image_url="http://example.com/dog.jpg",
            breed="test"
        )
        response = self.client.get('/api/favorites/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

