# iBR Tecnologia - API Rede Social

## Tecnologies
- Django
- Django Rest Framework

## To run
- Clone this repository
- Install and active virtual environment
- Execute: ```pip install -r requirements.txt```
- Then: ```python manage.py runserver```

## Endpoints
- "News":  
  * -- GET: http://127.0.0.1:8000/api/v1/news/
  * -- POST: http://127.0.0.1:8000/api/v1/news/
  * -- PUT: http://127.0.0.1:8000/api/v1/news/ID/
  * -- DELETE: http://127.0.0.1:8000/api/v1/news/ID/

- "Professionals": 
  * -- GET: http://127.0.0.1:8000/api/v1/professionals/
  * -- POST: http://127.0.0.1:8000/api/v1/professionals/
  * -- PUT: http://127.0.0.1:8000/api/v1/professionals/ID/
  * -- DELETE: http://127.0.0.1:8000/api/v1/professionals/ID/
  * -- SEARCH WITH CITY, NAME AND OR SPECIALITY: http://127.0.0.1:8000/api/v1/professionals/?speciality=VALUE&city=VALUE&name=VALUE

- "Professionals Addresses": 
  * -- GET: http://127.0.0.1:8000/api/v1/professionals-addresses/
  * -- POST: http://127.0.0.1:8000/api/v1/professionals-addresses/
  * -- PUT: http://127.0.0.1:8000/api/v1/professionals-addresses/ID/
  * -- DELETE: http://127.0.0.1:8000/api/v1/professionals-addresses/ID/

- "Professionals Contacts": 
  * -- GET: http://127.0.0.1:8000/api/v1/professionals-contacts/"
  * -- POST: http://127.0.0.1:8000/api/v1/professionals-contacts/"
  * -- PUT: http://127.0.0.1:8000/api/v1/professionals-contacts/ID/"
  * -- DELETE: http://127.0.0.1:8000/api/v1/professionals-contacts/ID/"


## Access Django's admin
- http://127.0.0.1:8000/admin/
