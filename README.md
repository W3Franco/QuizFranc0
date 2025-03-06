# Django Backend Project

## **Overview**
This is a Django-based backend API that includes user authentication, product management, and JWT-based authentication. It provides endpoints for retrieving users and products, along with secure authentication mechanisms.

## **Features**
- User authentication with JWT
- CRUD operations for products
- Secure API endpoints with permission classes
- Uses Django Rest Framework (DRF)

---

## **Installation and Setup**

### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo/backend
```

### **2. Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file in the root directory and add the following:
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
```

### **5. Apply Migrations**
```sh
python manage.py migrate
```

### **6. Create a Superuser (Admin Account)**
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

### **7. Run the Server**
```sh
python manage.py runserver
```

---

## **API Endpoints**

### **Authentication**
- `POST /api/token/` – Get access and refresh tokens
  - **Body:** `{ "username": "your_username", "password": "your_password" }`

### **User Routes**
- `GET /api/users/` – Get all users *(Requires Authentication)*
- `GET /api/users/<id>/` – Get a specific user *(Requires Authentication)*

### **Product Routes**
- `GET /api/products/` – Get all products
- `GET /api/products/<id>/` – Get a specific product

---

## **Testing with Postman**

### **1. Get an Access Token**
- **Method:** `POST`
- **URL:** `http://127.0.0.1:8000/api/token/`
- **Headers:** `Content-Type: application/json`
- **Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response:**
  ```json
  {
    "refresh": "your_refresh_token",
    "access": "your_access_token"
  }
  ```

### **2. Access Protected Routes**
- Add this header to requests:
  ```
  Authorization: Bearer your_access_token
  ```

---

## **Contributing**
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch and open a pull request

---
