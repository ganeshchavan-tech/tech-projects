# Task Manager API

This is a Django REST framework-based API for managing tasks and employees.

## How to Run the Project

1. Clone the repository:
    ```
    git clone <repository_url>
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory and add the following environment variables:
    ```
    DATABASE_NAME=<DATABASE_NAME>
    DATABASE_USER=<DATABASE_USER>
    DATABASE_PASSWORD=<DATABASE_PASSWORD>
    DATABASE_HOST=<DATABASE_HOST>
    ```
4. Apply migrations:
    ```
    python manage.py migrate
    ```
5. Create a superuser via terminal:
    ```
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```
    python manage.py runserver
    ```
7. Access the API at `http://localhost:8000/`.

## Database

- MySQL

## Dependencies

- Django==5.0.2
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.3.1
- mysqlclient==2.2.3
- python-dotenv==1.0.1
- django-cors-headers==4.3.1

## APIs

### Authentication

- **POST** `/login/`: Obtain JWT access token by providing username and password.
- **POST** `/logout/`: Invalidate refresh token to log out the user.
- **POST** `/token/refresh/`: Refresh JWT access token by providing refresh token.

### Accounts

- **GET** `/api/user/manage/`: Retrieve all user accounts (accessible only by admin).
- **POST** `/api/user/manage/`: Create a new user account (accessible only by admin).
- **PUT** `/api/user/manage/`: Update a user account (accessible only by admin).
- **DELETE** `/api/user/manage/{id}/`: Delete a user account (accessible only by admin).

### Employees

- **GET** `/api/user/employees/`: Retrieve all employees.
- **POST** `/api/user/employees/`: Create a new employee.
- **PUT** `/api/user/employees/{id}/`: Update an employee.
- **DELETE** `/api/user/employees/{id}/`: Delete an employee.

### Tasks

- **GET** `/api/tasks/`: Retrieve all tasks (accessible by admin and respective user).
- **POST** `/api/tasks/`: Create a new task (accessible by admin and respective user).

