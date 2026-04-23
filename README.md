# django_user_registration_system
User registration system built with Django (forms, validation, database integration).

##Register

User registration system built with Django. This project demonstrates form handling, server-side validation, and database integration using a modular app structure.

##Description

Register is a web application developed with Django that allows users to submit registration data through an HTML form. The application processes and validates the input, then stores it in a relational database. It is designed as a practical example of backend development using Django’s MVT architecture.

##Features
User registration form
Server-side data validation
Database storage using Django ORM
Modular structure with apps (nombre_app)
Basic error handling
Tech Stack
Python
Django
SQLite (default Django database)
HTML


Project Structure

register/

├── register/        # Project configuration (settings, urls)

├── nombre_app/      # Main app (models, views, forms)

    └── templates/       # HTML templates
    
├── db.sqlite3       # Database

└── manage.py


##Installation & Setup

Clone the repository and set up the environment:

git clone <your-repo-url>
cd register
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Usage

##Open your browser and go to:

http://127.0.0.1:8000/
Fill out the registration form
Submit the data
The system validates and stores the information in the database
Key Learnings
Understanding Django’s MVT architecture
Handling forms and POST requests
Implementing backend validation
Working with Django ORM and databases
Structuring a Django project using apps
Future Improvements
Add user authentication (login/logout)
Implement password hashing and security features
Add user roles and permissions
Improve frontend design (CSS/Bootstrap)
Build a REST API version with Django REST Framework
License

This project is open-source and available under the MIT License.
