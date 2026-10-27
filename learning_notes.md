
# Student Record Management API — Learning Notes

## 1. Introduction
This project is a Student Record Management API developed using Python and FastAPI. It allows users to create, view, update, and delete student records.

## 2. Technologies Used
- Python: Programming language used to develop the application.
- FastAPI: Framework used to build REST API endpoints.
- SQLite: Database used to store student records.
- Uvicorn: Server used to run the API.
- Swagger UI: Browser interface used to test API endpoints.

## 3. CRUD Operations
- **Create (POST):** Adds a new student record.
- **Read (GET):** Displays stored student records.
- **Update (PUT):** Modifies an existing student's details.
- **Delete (DELETE):** Removes a student record.

## 4. Database
The application uses SQLite and creates a `students` table containing an ID, name, age, and course. Student information is stored in the `students.db` database file.

## 5. API Authentication
The application uses an API key to protect the endpoints. The key is sent using the `X-API-Key` header. Requests with a valid key are accepted, while requests with a missing or invalid key receive an HTTP 401 response.

## 6. Input and Testing
The API accepts student information such as name, age, and course. Swagger UI at `/docs` allows the endpoints to be tested interactively.

## 7. What I Learned
- Creating REST API endpoints with FastAPI.
- Using SQLite to store and retrieve data.
- Implementing CRUD operations.
- Protecting endpoints with API-key authentication.
- Testing API responses using Swagger UI.

## 8. Conclusion
This project helped me understand how Python REST APIs work and how a database can be connected to an application for student record management.