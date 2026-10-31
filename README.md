# INF601 Mini Project 6
## Personal Task Manager

### Project Overview
This project is a web-based Personal Task Manager developed using Python and Django for INF601 - Advanced Programming in Python.

The application allows users to register, log in, create tasks, and monitor their task status through a personalized dashboard.

### Technologies Used
- Python 3.13
- Django 6.1.2
- SQLite
- HTML
- CSS
- Bootstrap 5
- Git and GitHub

### Features
- User registration
- User login and logout
- User authentication
- Create personal tasks
- View tasks on a dashboard
- Display pending and completed task status
- User-specific task management
- Persistent SQLite database storage

### Installation Instructions

1. Clone the repository:

   git clone https://github.com/Bucey01/miniproject6AdeolaAjayi.git

2. Navigate into the project:

   cd miniproject6AdeolaAjayi

3. Create a virtual environment:

   python3 -m venv venv

4. Activate the virtual environment:

   macOS/Linux:
   source venv/bin/activate

   Windows:
   venv\Scripts\activate

5. Install dependencies:

   python -m pip install -r requirements.txt

6. Generate a Django secret key and save it in a local .env file:

   python -c "from django.core.management.utils import get_random_secret_key; from pathlib import Path; Path('.env').write_text('DJANGO_SECRET_KEY=' + get_random_secret_key() + '\n')"

7. On macOS/Linux, load the environment variable:

   set -a
   source .env
   set +a

8. Apply database migrations:

   python manage.py migrate

9. Start the development server:

   python manage.py runserver

10. Open the application:

   http://127.0.0.1:8000/

Note: On Windows, set the DJANGO_SECRET_KEY environment variable using the appropriate shell before running Django.

### Testing
The following functionality was tested successfully:
- Django system check
- Database migrations
- Homepage rendering
- User registration
- User login
- Task creation
- Dashboard display
- Task persistence after logout and login

### Security
The Django secret key is stored in a local .env file and is not committed to GitHub.

The SQLite database and Python virtual environment are excluded using .gitignore.

This application uses Django's development server and is intended for educational purposes.

### AI Assistance Disclosure

**Work Completed Independently**

I personally worked on developing, configuring, and testing my Personal Task Manager application using Python and Django. I accessed the FHSU Linux development environment, created the Django project structure, executed commands, and tested the application functionality.

I tested user registration, login, task creation, dashboard functionality, and task persistence. I uploaded the project to GitHub, cloned it onto my personal MacBook, configured the Python virtual environment, installed dependencies, and successfully ran the application locally.

**How AI Was Used**

I used ChatGPT as a learning and development assistance tool. ChatGPT provided explanations, Python and HTML code examples, guidance for configuring Django views, URLs, forms, authentication, and database settings, and troubleshooting assistance.

ChatGPT also helped with GitHub commands, environment configuration, testing procedures, and README documentation.

**My Role in the Development Process**

I was responsible for executing commands, incorporating and reviewing suggested code, configuring the development environments, testing the application, troubleshooting issues with AI guidance, and verifying the final results.

AI served as a supporting educational resource throughout the project.

### Course Information
INF601 - Advanced Programming in Python

Mini Project 6 - Personal Task Manager
