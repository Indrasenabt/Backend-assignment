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

1.  **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    # Windows:
    .\.venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run migrations**:
    ```bash
    python manage.py migrate
    ```

4.  **Start the development server**:
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

## Complete API Testing Examples

### 1. Register a User
**Endpoint:** `POST http://127.0.0.1:8000/api/auth/register/`

**Request Body:**
```json
{
  "username": "Howard",
  "password": "Howard123"
}
```

**Response (201 Created):**
```json
{
  "user": {
    "id": 6,
    "username": "Howard",
    "email": ""
  },
  "message": "User registered successfully"
}
```

### 2. Login User
**Endpoint:** `POST http://127.0.0.1:8000/api/auth/login/`

**Request Body:**
```json
{
  "username": "Howard",
  "password": "Howard123"
}
```

**Response (200 OK):**
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MTc3Mjg3OSwiaWF0IjoxNzgxMTY4MDc5LCJqdGkiOiIwYjZmNzgyMWY1YTc0YTE4ODRjMmY0MjllZjcyZDcyZSIsInVzZXJfaWQiOiI2In0.R2r6nq-34BaiNv04IM8SHobULLcfFzdE_GV_fIA31Zk",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxMjU0NDc5LCJpYXQiOjE3ODExNjgwNzksImp0aSI6IjQ0NWNlZmY0YjA0ZTQxNmQ5OTgwODNmNDg3YzMyNDYyIiwidXNlcl9pZCI6IjYifQ.xRs2T3t8YHZWdExL57zbeoT0FXF5ZyrFVlfVSl2P3mg"
}
```

### 3. Get Random Dog Image
**Endpoint:** `GET http://127.0.0.1:8000/api/dogs/random/`

**Response (200 OK):**
```json
{
  "image_url": "https://images.dog.ceo/breeds/terrier-andalusian/images.jpg",
  "breed": "terrier-andalusian"
}
```

### 4. Get Dog Images by Breed
**Endpoint:** `GET http://127.0.0.1:8000/api/dogs/breed/labrador/`

**Response (200 OK):**
```json
[
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_2234.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_2897.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_3301.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_3613.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_3753.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_4403.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_4462.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_5941.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_854.jpg",
    "breed": "labrador"
  },
  {
    "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_9374.jpg",
    "breed": "labrador"
  }
]
```

### 5. Get All Favorites (Authenticated)
**Endpoint:** `GET http://127.0.0.1:8000/api/favorites/`

**Headers:**
```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Response (200 OK):** 
```json
[]
```
*(Empty array if no favorites created yet)*

### 6. Create a Favorite (Authenticated)
**Endpoint:** `POST http://127.0.0.1:8000/api/favorites/`

**Headers:**
```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "image_url": "https://images.dog.ceo/breeds/hound-english/n02089973_1132.jpg",
  "breed": "hound-english",
  "notes": "Beautiful dog!",
  "tags": ["hound1", "Hindi", "indoor"]
}
```

**Response (201 Created):**
```json
{
  "id": 6,
  "user": "Howard",
  "image_url": "https://images.dog.ceo/breeds/hound-english/n02089973_1132.jpg",
  "breed": "hound-english",
  "notes": "Beautiful dog!",
  "tags": [
    "hound1",
    "Hindi",
    "indoor"
  ],
  "created_at": "2026-06-11T09:03:57.114177Z"
}
```

### 7. Update a Favorite (Authenticated)
**Endpoint:** `PATCH http://127.0.0.1:8000/api/favorites/6/`

**Headers:**
```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "notes": "Updated notes and tag!",
  "tags": ["update2", "tags2"]
}
```

**Response (200 OK):**
```json
{
  "notes": "Updated notes and tag!",
  "tags": [
    "update2",
    "tags2"
  ]
}
```

**Fetch Updated Favorite:**
```json
{
  "id": 6,
  "user": "Howard",
  "image_url": "https://images.dog.ceo/breeds/hound-english/n02089973_1132.jpg",
  "breed": "hound-english",
  "notes": "Updated notes and tag!",
  "tags": [
    "update2",
    "tags2"
  ],
  "created_at": "2026-06-11T09:03:57.114177Z"
}
```

### 8. Delete a Favorite (Authenticated)
**Endpoint:** `DELETE http://127.0.0.1:8000/api/favorites/6/`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

**Response (204 No Content):**
*(No body - successful deletion)*

## Git Commands for Version Control

```bash
# Check repository status
git status

# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "Your descriptive message here"

# Push to remote repository
git push origin main
```

register

 API -- POST http://127.0.0.1:8000/api/auth/register/
 {  
    "username": "Howard",  
    "password": "Howard123"
}

response:

{
    "user": {
        "id": 6,
        "username": "Howard",
        "email": ""
    },
    "message": "User registered successfully"
}

login
 API POST -- http://127.0.0.1:8000/api/auth/login/
 
 body:
 {
  "username": "Howard",
  "password": "Howard123"
}

respone:

 {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MTc3Mjg3OSwiaWF0IjoxNzgxMTY4MDc5LCJqdGkiOiIwYjZmNzgyMWY1YTc0YTE4ODRjMmY0MjllZjcyZDcyZSIsInVzZXJfaWQiOiI2In0.R2r6nq-34BaiNv04IM8SHobULLcfFzdE_GV_fIA31Zk",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxMjU0NDc5LCJpYXQiOjE3ODExNjgwNzksImp0aSI6IjQ0NWNlZmY0YjA0ZTQxNmQ5OTgwODNmNDg3YzMyNDYyIiwidXNlcl9pZCI6IjYifQ.xRs2T3t8YHZWdExL57zbeoT0FXF5ZyrFVlfVSl2P3mg"
}

to get random dog image

GET -- http://127.0.0.1:8000/api/dogs/random/
repone: 
{
    "image_url": "https://images.dog.ceo/breeds/terrier-andalusian/images.jpg",
    "breed": "terrier-andalusian"
}

get by breed

GET http://127.0.0.1:8000/api/dogs/breed/labrador/
repone:
[
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_2234.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_2897.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_3301.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_3613.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_3753.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_4403.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_4462.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_5941.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_854.jpg",
        "breed": "labrador"
    },
    {
        "image_url": "https://images.dog.ceo/breeds/labrador/n02099712_9374.jpg",
        "breed": "labrador"
    }
]

get all favourites:

GET     http://127.0.0.1:8000/api/favorites/
Authorization: Bearer <your_access_token>

repone:[] a e havent created favourite yet

Create a Favorite (Authenticated)

POST http://127.0.0.1:8000/api/favorites/
Headers: Content-Type: application/json
Authorization: Bearer <your_access_token>
Body:


repone:
{
    "id": 6,
    "user": "Howard",
    "image_url": "https://images.dog.ceo/breeds/hound-english/n02089973_1132.jpg",
    "breed": "hound-english",
    "notes": "Beautiful dog!",
    "tags": [
        "hound1",
        "Hindi",
        "indoor"
    ],
    "created_at": "2026-06-11T09:03:57.114177Z"
}

Update a Favorite (Authenticated)
PATCH  http://127.0.0.1:8000/api/favorites/1/
Headers:
Content-Type: application/json
Authorization: Bearer <your_access_token>
Body:
 {
  "notes": "Updated notes and tag!",
  "tags": ["update2", "tags2"]
}

repone: {
    "notes": "Updated notes and tag!",
    "tags": [
        "update2",
        "tags2"
    ]
}

after update hen e fetch a favourite:
{
    "id": 6,
    "user": "Howard",
    "image_url": "https://images.dog.ceo/breeds/hound-english/n02089973_1132.jpg",
    "breed": "hound-english",
    "notes": "Updated notes and tag!",
    "tags": [
        "update2",
        "tags2"
    ],
    "created_at": "2026-06-11T09:03:57.114177Z"
}

for delete 

Method:http://127.0.0.1:8000/api/favorites/6/
Headers:
Authorization: Bearer {{access_token}}
reponse:
204 No Content


git status


git add .


git commit -m "Your descriptive message here"

git push origin main