import requests

class DogAPIService:
    BASE_URL = "https://dog.ceo/api"

    @staticmethod
    def get_random_image():
        response = requests.get(f"{DogAPIService.BASE_URL}/breeds/image/random")
        if response.status_code == 200:
            data = response.json()
            image_url = data.get('message')
            # Extract breed from URL if possible
            # Format: https://images.dog.ceo/breeds/hound-english/n02089973_1132.jpg
            breed = None
            if 'breeds/' in image_url:
                breed = image_url.split('breeds/')[1].split('/')[0]
            return {
                "image_url": image_url,
                "breed": breed
            }
        return None

    @staticmethod
    def get_images_by_breed(breed):
        response = requests.get(f"{DogAPIService.BASE_URL}/breed/{breed}/images/random/10")
        if response.status_code == 200:
            data = response.json()
            images = data.get('message', [])
            return [{"image_url": img, "breed": breed} for img in images]
        return []
