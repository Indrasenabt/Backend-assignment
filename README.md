# Pet Gallery Tracker API

A RESTful API service built with Django and Django REST Framework for managing favorite dog images.

## Features
- User registration and login (JWT Authentication).
- Integration with external Dog API (dog.ceo).
- CRUD operations for user's favorite dog images.
- Images can have optional notes and tags.

## Prerequisites
- Python 3.10+
- `venv` (recommended)

## Setup Instructions

1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd pet-gallery
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server**:
    ```bash
    python manage.py runserver
    ```

## API Documentation

### Authentication
- `POST /api/auth/register/`: Register a new user.
- `POST /api/auth/login/`: Login and receive JWT tokens (access & refresh).
- `POST /api/auth/token/refresh/`: Refresh the access token.

### External Dog API
- `GET /api/dogs/random/`: Fetch a random dog image and its breed.
- `GET /api/dogs/breed/<str:breed>/`: Fetch up to 10 random images for a specific breed.

### User Favorites (Authenticated)
All endpoints below require an `Authorization: Bearer <access_token>` header.

- `POST /api/favorites/`: Add a favorite image.
    - Fields: `image_url` (required), `breed`, `notes`, `tags` (JSON list).
- `GET /api/favorites/`: View all saved favorites for the current user.
- `GET /api/favorites/<id>/`: Retrieve a single favorite item.
- `PATCH /api/favorites/<id>/`: Update notes and tags for a favorite.
- `DELETE /api/favorites/<id>/`: Delete a favorite item.

## Example Request (Create Favorite)
```json
{
  "image_url": "https://images.dog.ceo/breeds/hound-english/n02089973_1132.jpg",
  "breed": "hound-english",
  "notes": "Beautiful dog!",
  "tags": ["hound", "english", "outdoor"]
}
```
