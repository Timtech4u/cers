# CERS

## [Hosted App](https://cers-app.herokuapp.com)

## Setup
- Clone the repo and change to project directory:
- Install dependencies: `pip install -r requirements.txt`
- Migrate database: `python manage.py migrate`
- Create super user: `python manage.py createsuperuser`
- Run server: `python manage.py runserver`
- If you need to import new locations, run `python manage.py importer`

## Technologies
- Python/Django
- USSD
- Firebase
- Web
- Map
