![GuideMate Banner](GuideMate.png)
# Attendance Monitoring System - Student Attendance Management Web App

A Django-based web application for managing and monitoring student attendance
with a clean dashboard, full student CRUD operations, and real-time
present/absent tracking.

Built as a Web Development Project using Python Django at Ilahia College of
Engineering and Technology, under APJ Abdul Kalam Technological University,
Kerala.

---

## Project Structure

```
Attendance Monitoring System/
│
├── tr/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── userapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login_page.html
│   │   ├── signup_page.html
│   │   ├── dashboard.html
│   │   ├── students_list.html
│   │   ├── create_student.html
│   │   ├── edit_student.html
│   │   └── attendence.html
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── apps.py
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## How It Works

**Authentication**
- Staff can register and log in with a username and password
- Login-protected dashboard using Django's built-in auth system
- Secure sign-out functionality

**Dashboard**
- Displays total students, students present, and students on leave
- Live count updated based on daily attendance records

**Student Management**
- Add new students with full profile details (name, course, age, DOB, DOJ, address)
- View the complete list of all registered students
- Edit or delete any student record

**Attendance Tracking**
- Mark each student as Present or Absent for the current date
- Attendance records stored with date stamps
- Dashboard reflects today's present/absent counts in real time

---

## Setup Instructions

1. Clone this repository

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in your values:
   ```
   SECRET_KEY=your-secret-key-here
   DB_NAME=your-db-name
   DB_USER=your-db-user
   DB_PASSWORD=your-db-password
   DB_HOST=localhost
   DB_PORT=3306
   DEBUG=True
   ```

5. Create the MySQL database with the name you set in `DB_NAME`

6. Run migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```
   python manage.py runserver
   ```

9. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Pages & Routes

| URL | Page | Description |
|---|---|---|
| `/` | Login | Staff login page |
| `/signup/` | Sign Up | Register a new staff account |
| `/dashboard` | Dashboard | Overview of attendance stats |
| `/students_list/` | Students List | View all registered students |
| `/create_student/` | Add Student | Register a new student |
| `/edit_student/<id>` | Edit Student | Update student details |
| `/delete_student/<id>` | Delete Student | Remove a student record |
| `/attendece/` | Attendance | Mark present or absent |
| `/admin/` | Django Admin | Full admin panel |

---

## Database Models

**Student**
- Name, Age, Date of Birth, Date of Joining
- Course, Address, City, State, Country
- Active status, Leave count, On-leave flag

**Student Attendance**
- Name, Course
- Date, Attendance status (1 = Present, 0 = Absent)

---

## Tech Stack
- **Backend:** Python, Django 4.2
- **Database:** MySQL
- **Frontend:** HTML, CSS (Django Templates)
- **Auth:** Django Built-in Authentication
- **Config:** python-decouple (.env support)

---

## Author
Althaf Ameen Haneefa
B.Tech — Artificial Intelligence and Data Science
Ilahia College of Engineering and Technology, Muvattupuzha
2025

---

## License
This project is licensed under the MIT License.
