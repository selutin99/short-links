# short-links
 Web application providing API for short links service

### Technology stack
- Flask v1.1.2
- SQLAlchemy v2.4.4
- PostgreSQL v9.6.18

## Manual installation
### Initialize project environment

    virtualenv venv
    For Windows: CALL venv/Scripts/activate
    For Linux: source venv/bin/activate
    pip install -r requirements.txt


### Initializing the Database
       
    # Create DB
    python manage.py init_db
    # Migrate DB tables
    python manage.py db upgrade


### Running the app

    # Start the Flask development web server
    python manage.py runserver
