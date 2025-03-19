# Todo Application with Django and Celery

## Stack
- Django + DRF (Spetacular)
- Celery + RabbitMQ
- PostgreSQL
- Docker Compose

## How to run

1. Make sure you have **Docker** and **Docker Compose** installed.
2. In the project directory, run:
```bash
docker-compose up --build
```


##Endpoints da API
POST /api/tasks/ - Create a new task.
GET /api/tasks/ - Retrieve all tasks.
GET /api/tasks/{id}/ - Retrieve a specific task.
PUT /api/tasks/{id}/ - Fully update a task (all fields).
PATHS /api/tasks/{id}/ - Partially update a task (only specified fields).
DELETE /api/tasks/{id}/ - Delete a task.

# How to Use the Todo API

This API allows you to manage tasks using Django REST Framework (DRF). It supports creating, retrieving, updating, and deleting tasks, and also includes a Celery task that periodically checks for old incomplete tasks.

---

## Accessing the API Documentation (Swagger UI)
The API provides an interactive documentation using **drf-spectacular**. You can access it via:

🔹 **Swagger UI:**  
`http://localhost:8000/docs/`

🔹 **ReDoc (alternative UI):**  
`http://localhost:8000/redoc/`

These pages allow you to test API endpoints directly from the browser.

---

## API Endpoints

### **1️⃣ Create a Task**
- **Method:** `POST`
- **URL:** `/api/tasks/`
- **Description:** Creates a new task.
- **Request Body (JSON):**
```json
    {
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": false, (optional - default is false)
    }
```

- **Response Body (JSON):**
```json
    {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": false,
    "created_at": "2025-03-19T12:00:00Z",
    "updated_at": "2025-03-19T12:00:00Z"
    }
```

### **2️⃣ Retrieve All Tasks**
- **Method:** `GET`
- **URL:** `/api/tasks/`
- **Description:** Fetches all tasks.

- **Response Body (JSON):**
```json
    [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, bread, eggs",
        "completed": false,
        "created_at": "2025-03-19T12:00:00Z",
        "updated_at": "2025-03-19T12:00:00Z"
    },
    {
        "id": 2,
        "title": "Walk the dog",
        "description": "Take Bruno for a walk",
        "completed": true,
        "created_at": "2025-03-18T14:30:00Z",
        "updated_at": "2025-03-18T15:00:00Z"
    }
    ]
```

### **3️⃣ Retrieve a Specific Task**
- **Method:** `GET`
- **URL:** `/api/tasks/{id}`
- **Description:** Fetches all tasks.
GET /api/tasks/1/

- **Response Body (JSON):**
```json
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, bread, eggs",
        "completed": false,
        "created_at": "2025-03-19T12:00:00Z",
        "updated_at": "2025-03-19T12:00:00Z"
    }
```

### **4️⃣ Update a Task (Full Update)**
- **Method:** `PUT`
- **URL:** `/api/tasks/{id}`
- **Description:** Updates all fields of a task.
PUT /api/tasks/1/

- **Request Body (JSON):**
```json
    {
    "title": "Buy groceries",
    "description": "Milk, bread, eggs, butter",
    "completed": true
    }
```

- **Response Body (JSON):**
```json
    {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs, butter",
    "completed": true,
    "created_at": "2025-03-19T12:00:00Z",
    "updated_at": "2025-03-19T12:05:00Z"
    }
```

### **5️⃣ Update a Task (Partial Update)**
- **Method:** `PATCH`
- **URL:** `/api/tasks/{id}`
- **Description:** Updates only specified fields.
PATCH /api/tasks/1/

- **Request Body (JSON):**
```json
    {
    "completed": false
    }
```

- **Response Body (JSON):**
```json
    {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs, butter",
    "completed": false,
    "created_at": "2025-03-19T12:00:00Z",
    "updated_at": "2025-03-19T12:07:00Z"
    }
```

### **6️⃣ Delete a Task**
- **Method:** `DELETE`
- **URL:** `/api/tasks/{id}`
- **Description:** Deletes a specific task.
DELETE /api/tasks/1/

- **Response**
204 No Content (successful deletion)
