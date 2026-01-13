# Bloggy - A Blog Application

![Banner](https://github.com/user-attachments/assets/e7cff79a-6b75-408f-b479-224159c241cc)


Bloggy is a clean and beginner-friendly blog web application built with Django.
It allows users to create, read, update, and delete blog posts with authentication and a modern UI styled using Tailwind CSS.

## Features

- User authentication (Signup, Login, Logout)
- Create, update, and delete blog posts
- View all blog posts with latest posts on top
- Dedicated post detail (Read More) page
- Category support for blog posts
- Clean and responsive UI

## Tech Stack

- Frontend: HTML, Tailwind CSS
- Backend: Django
- Database: SQLite
- Authentication: Django built-in authentication system

## Installation and Setup

Follow these steps to run the project locally.

#### 1. Clone the repository
```
git clone https://github.com/hello-abdul-manan/todo-app.git
cd todo-app
```

#### 2. Create and activate virtual environment
```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

#### 3. Install dependencies
```
pip install django
```

#### 4. Run migrations
```
cd blog_app
python manage.py makemigrations
python manage.py migrate
```

#### 5. Run Tailwind CSS build
```
npx tailwindcss -i ./blog_app/static/src/input.css -o ./blog_app/static/src/output.css --watch
```

#### 6. Start the development server
```
python manage.py runserver
```

#### 7. Visit the app at:
```
http://127.0.0.1:8000/bloggy/
```

## Author  

**Abdul Manan Maqsood**  
- [GitHub](https://github.com/hello-abdul-manan)  
- [LinkedIn](https://www.linkedin.com/in/helloabdulmanan/)

## License  

This project is open source and available for learning and personal use.

---
