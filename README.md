# short-links
 Web application providing API for short links service

### Technology stack
- Python 3.6.12
- Flask v1.1.2
- SQLAlchemy v2.4.4
- PostgreSQL v9.6.18

## Docker installation

    docker-compose build
    docker-compose up -d
    
    # First start
    docker-compose exec app python manage.py init_db
    docker-compose exec app python manage.py db upgrade
    docker-compose exec app python -m pytest

Application will be available by address: 127.0.0.1:5000/

## Manual installation
### Initialize project environment

    pip install virtualenv
    virtualenv venv
    For Windows: CALL venv/Scripts/activate
    For Linux: source venv/bin/activate
    pip install -r requirements.txt


### Initialize the Database
       
    # Create DB
    python manage.py init_db
    # Migrate DB tables
    python manage.py db upgrade

### Run the tests

    # Start the API validaing tests
    python -m pytest


### Run the app

    # Start the Flask development web server
    python manage.py runserver
 
Application will be available by address: 127.0.0.1:5000/ 

## Swagger
After server starts you can move to swagger API description page by the next url

    <APP:HOST><APP:PORT>/swagger
![alt text](https://i.ibb.co/W5p27s0/image.png)

## Configuration
You can set environment variables 
to change configuration of application (or use default settings)  
- SECRET_KEY - secret token of application
- POSTGRES_URL - url of postgre server
- POSTGRES_USER - user of postgre server
- POSTGRES_PW - password of user
- POSTGRES_DB - database of application in postgre
- FLASK_ENV - environment of application. Possible values:
   * config.DevelopmentConfig - config with enabled debug and CORS
   * config.ProductionConfig - config with disabled debug
