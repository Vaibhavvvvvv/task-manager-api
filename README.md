# Task Manager API

A RESTful API built using Django and Django REST Framework for managing tasks with JWT authentication.

---

## Objective

Build a RESTful API for a simple task manager application that supports:

- Task CRUD operations
- User authentication
- API documentation
- Unit testing
- Pagination and filtering (bonus)

---

# Task Model

The Task model contains the following fields:

- id (auto-generated primary key)
- title (string)
- description (text)
- completed (boolean)
- created_at (timestamp)
- updated_at (timestamp)
- user (ForeignKey to User)

---

# API Endpoints

Base URL:
http://127.0.0.1:8000/api/

## Authentication

### Register User
POST /api/register/

Request:
{
  "username": "testuser",
  "password": "testpassword123"
}

Response:
{
  "message": "User created successfully"
}

---

### Login (JWT)
POST /api/login/

Request:
{
  "username": "testuser",
  "password": "testpassword123"
}

Response:
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}

---

# Task Endpoints

(Requires JWT Authentication)

### Get All Tasks
GET /api/tasks/

### Get Single Task
GET /api/tasks/{id}/

### Create Task
POST /api/tasks/

Request:
{
  "title": "My Task",
  "description": "Complete assignment",
  "completed": false
}

### Update Task
PUT /api/tasks/{id}/

### Delete Task
DELETE /api/tasks/{id}/

---

# Authentication Rules

- JWT Authentication is implemented using SimpleJWT.
- Only authenticated users can:
  - Create tasks
  - Update tasks
  - Delete tasks
- Users can only access their own tasks.
- Admin users can access all tasks.

---

# Pagination (Bonus Feature)

Pagination is enabled using PageNumberPagination.

Default page size: 5

Example:
GET /api/tasks/?page=2

Response includes:
- count
- next
- previous
- results

---

# Filtering (Bonus Feature)

Tasks can be filtered by completed status:

GET /api/tasks/?completed=true
GET /api/tasks/?completed=false

---

# API Documentation

Swagger documentation is available at:

http://127.0.0.1:8000/swagger/

Steps to use:
1. Register a user
2. Login to get JWT access token
3. Click "Authorize"
4. Enter:
   Bearer <your_access_token>
5. Test endpoints using "Try it out"

---

# Installation & Setup

## 1. Clone Repository

git clone <https://github.com/Vaibhavvvvvv/task-manager-api>
cd task-manager-api

## 2. Create Virtual Environment

python -m venv .venv
.venv\Scripts\activate  (Windows)

## 3. Install Dependencies

pip install -r requirements.txt

## 4. Apply Migrations

python manage.py migrate

## 5. Run Server

python manage.py runserver

---

# Running Unit Tests

To run tests:

python manage.py test tasks

The test cases verify:

- Task creation
- Task listing
- Task deletion
- JWT authentication
- Access restrictions between users

---

# Project Structure

task-manager-api/
│
├── config/
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md

---

# Additional Notes

- The API is fully RESTful.
- JWT-based authentication ensures secure access.
- Swagger provides interactive documentation.
- Unit tests ensure API correctness.
- Pagination and filtering improve usability.

---

# Submission

GitHub repository link:
<https://github.com/Vaibhavvvvvv/task-manager-api>