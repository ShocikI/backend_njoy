# njoy_backend

A Django REST Framework backend for user registration and profile management, featuring secure authentication and user profile updates.

## Requirements

- Python 3.10+
- Django 4.x
- Django REST Framework
- django-postgis (for EncryptedTokenAuthentication)
- Pillow (for image/avatar support)
- Other dependencies as required by your project

## Installation

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Registration

- `POST /users/`  
  Register a new user.

### Retrieve User

- `GET /users/<username>/`  
  Retrieve user profile by username.

### Update User

- `PATCH /users/<username>/`  
  Update either the avatar or description (only one at a time).

  **Request Example:**

  ```json
  {
    "avatar": "<file>"
  }
  ```

  or

  ```json
  {
    "description": "New description"
  }
  ```

## Authentication

This project uses `EncryptedTokenAuthentication` from `django_postgis`. Ensure you have the correct authentication setup in your client requests.

## Notes

- Only one field (`avatar` or `description`) can be updated at a time.
- When updating the avatar, the old avatar file is deleted from the server if a new one is uploaded.

