# iBR Tecnologia - API Social Network

## Tecnologies
- Django
- Django Rest Framework

## To run locally
- Clone this repository
- Install and active a virtual environment
- Execute: ```docker-compose build```
- Execute: ```docker-compose up```

## Endpoints
- "Posts":  
  * -- GET: http://127.0.0.1:8000/api/v1/posts/
  * -- POST: http://127.0.0.1:8000/api/v1/posts/
  * -- PUT: http://127.0.0.1:8000/api/v1/posts/ID/
  * -- DELETE: http://127.0.0.1:8000/api/v1/posts/ID/

- "Users" (only admin can access): 
  * -- GET: http://127.0.0.1:8000/api/v1/users/
  * -- POST: http://127.0.0.1:8000/api/v1/users/
  * -- PUT: http://127.0.0.1:8000/api/v1/users/ID/
  * -- DELETE: http://127.0.0.1:8000/api/v1/users/ID/

- "Regiser an user":
  * -- ENDPOINT: http://127.0.0.1:8000/register/

## Making a request
- Login: http://127.0.0.1:8000/login/
  - Send json with username and password and get your token 
- Choose an endpoint
- You can use postman, insomnia or any other API tool
- On header, include:
  - Authorization | Bearer <token>
- On post's image:
  - Send a multipart-form

## Testing API
- Create a post
- Run: ```pytest posts/test/test_api.py```

## Access Django's admin
- http://127.0.0.1:8000/admin/
  - User: admin
  - Pass: admin
