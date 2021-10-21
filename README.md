# iBR Tecnologia - API Social Network

## Tecnologies
- Django
- Django Rest Framework

## To run
- Clone this repository
- Install and active virtual environment
- Execute: ```pip install -r requirements.txt```
- Then: ```python manage.py runserver```

## Endpoints
- "Posts":  
  * -- GET: http://127.0.0.1:8000/api/v1/posts/
  * -- POST: http://127.0.0.1:8000/api/v1/posts/
  * -- PUT: http://127.0.0.1:8000/api/v1/posts/ID/
  * -- DELETE: http://127.0.0.1:8000/api/v1/posts/ID/

- "Users": 
  * -- GET: http://127.0.0.1:8000/api/v1//
  * -- POST: http://127.0.0.1:8000/api/v1/users/
  * -- PUT: http://127.0.0.1:8000/api/v1/users/ID/
  * -- DELETE: http://127.0.0.1:8000/api/v1/users/ID/

## Making a request
- Choose an endpoint
- You can use postman, insomnia or any other API tool
- On header, include:
  - Authorization | Bearer <token>

## Access Django's admin
- http://127.0.0.1:8000/admin/
