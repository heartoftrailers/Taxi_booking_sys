# Taxi_booking_sys

# delete .db
# cd taxi_booking_sys

virtualenv venv 
# or this instead: python -m virtualenv venv
source ./venv/bin/activate
pip install -r  requirements.txt
python manage.py migrate
python manage.py makemigrations
python manage.py migrate --run-syncdb
```
## Running locally
```bash
python manage.py runserver

## Tests
```bash
python manage.py test
```
