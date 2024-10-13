
# URL Shortener Project

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Security Notes](#security-notes)
- [License](#license)

---

## Project Overview
This project is a URL shortener built using Django, with separate API endpoints for authenticated and unauthenticated users to shorten URLs. It supports user registration, authentication, and password management using Django Knox for token-based authentication.

---

## Features
- Shorten URLs for both authenticated and unauthenticated users.
- CSV file upload for bulk URL shortening.
- User authentication (Registration, Login, Logout).
- Token-based authentication with Django Knox.
- Password reset and change functionality.
- Detailed API views for CRUD operations on URLs.

---

## Technologies Used
- Python 3.x
- Django 4.x
- Django REST Framework
- Django Knox (for token-based authentication)
- SQLite (default database, can be replaced with PostgreSQL or MySQL)
- RESTful APIs

---

## Installation

### Prerequisites
- Python 3.x
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:
    ```
    git clone <repository_url>
    cd url_shortener_project
    ```

2. Create a virtual environment:
    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Set up environment variables for email settings (e.g., `.env` file):
    ```
    EMAIL_HOST_USER=<your_email>
    EMAIL_HOST_PASSWORD=<your_password>
    ```

5. Apply migrations:
    ```
    python manage.py migrate
    ```

6. Run the development server:
    ```
    python manage.py runserver
    ```

---

## Project Structure

```
url_shortener_project/
│
├── url_shortener/        # Main app for URL shortening
│   ├── models.py         # Models for URL mapping
│   ├── views.py          # API Views for URL shortening
│   ├── urls.py           # Routes for URL-related operations
│
├── user/                 # App for User management
│   ├── models.py         # User models (custom user model if needed)
│   ├── views.py          # User authentication views (Registration, Login, etc.)
│   ├── urls.py           # Routes for user-related operations
│
├── url_shortener_project/ # Main Django project settings
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project-wide URL configurations
│   ├── wsgi.py           # WSGI application entry point
│
├── manage.py             # Django's CLI command utility
├── requirements.txt      # Required Python packages
└── README.md             # This README file
```

---

## Usage

### Shorten a URL (Unauthenticated User)
Make a `POST` request to `/u/` with a `long_url` to receive a shortened URL.

### Shorten a URL (Authenticated User)
1. First, register or log in to receive a token.
2. Use the token in your `Authorization` header to make authenticated requests.

---

## API Endpoints

### URL Operations
- `GET /urlmapping-unauth-list/`: Retrieve all shortened URLs (unauthenticated).
- `POST /urlmapping-unauth-create/`: Shorten a URL without authentication.
- `GET /urlmapping-auth-list/`: Retrieve all shortened URLs (authenticated).
- `POST /urlmapping-auth-create/`: Shorten a URL with authentication.

### User Authentication
- `POST /register/`: Register a new user.
- `POST /login/`: Log in to receive a token.
- `POST /logout/`: Log out and invalidate the token.
- `POST /reset-password/`: Reset password (email required).
- `POST /set-new-password/<uid>/<token>/`: Set new password after reset.

---

## Authentication
This project uses Django Knox for token-based authentication. Once logged in, you will receive a token that must be included in the `Authorization` header for authenticated API requests.

Example header:
```
Authorization: Token <your_token>
```

---

## Security Notes
- Ensure `DEBUG` is set to `False` in production.
- Keep your `SECRET_KEY` and email credentials safe.
- Set up proper database and email configurations before deployment.

---

## License
This project is licensed under the MIT License.