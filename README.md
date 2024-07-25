### Api service for chat

###  Install  and create db
```shell
git clone https://github.com/tkachuk2291/chat-team.git
``` 
```shell
cd ChatTeam
```
```shell
python3 -m venv venv  
``` 
```shell
source venv/bin/activate  
```
```shell
pip install -r requirements.txt  
```
### Setting up Environment Variables
```shell
touch .env  
```
### Example of environment variables
``` 
 .env.sample 
```
**Here you can generate your secret key** 
https://djecrety.ir/ 
``` 
set DJANGO_SECRET_KEY='your_secret_key'
set DATABASE_URL="secret_key" (if you are developer please contact with me i'll give you a key)
```

```shell
python manage.py migrate  
```
```shell
python manage.py runserver 8002 
```

### Local
http://127.0.0.1:8000/

### Chat endpoint & JWT Token

**Chat endpoint**

"chat": http://127.0.0.1:8000/chat/,  
"category": http://127.0.0.1:8000/category/,  
"message":http://127.0.0.1:8000/message/
user registration: http://127.0.0.1:8000/user/
user login : http://127.0.0.1:8000/user1/login/

**JWT Token**

Use format Authorization | Bearer and token  
![img.png](img.png)  

Please note if you get access for browser install modheader (https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj),

If you use postman don't forget put aces key in headers , when you login email|password credentials.
![img_1.png](img_1.png)  

Example aces for Jwt-Token : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMzQyMzY3LCJpYXQiOjE3MjE5MTAzNjcsImp0aSI6ImZlYTc3M2E3ZDQ5MTQ4Y2E4NjM5OTllY2MzZDIxODk1IiwidXNlcl9pZCI6MX0.yyCnIF9vkU-wDlu-3xd9Ry4QlmllnglVUgZprQBmLoA"











