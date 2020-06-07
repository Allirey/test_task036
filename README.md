## test task "Social Network"

#### api endpoints:

##### users:

```
http://localhost:8000/api/users/ [GET, POST]
http://localhost:8000/api/users/{user_id}/ [GET, PUT, PATCH, DELETE]
http://localhost:8000/api/users/{user_id}/ [GET]
http://localhost:8000/api/users/activity{user_id}/ [GET]
```

##### posts:
```
http://localhost:8000/api/posts/ [GET, POST]
http://localhost:8000/api/posts/{post_id}/ [GET, PUT, PATCH, DELETE]
http://localhost:8000/api/posts/{post_id}/like [POST]
http://localhost:8000/api/posts/{post_id}/unlike/ [POST]
http://localhost:8000/api/posts/analytics?date_from={YYYY-MM-DD}&date_to={YYYY-MM-DD} [GET]
```

## usage / demo:

```shell script
git clone https://github.com/Allirey/test_task036 && cd test_task036/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
./demo_bot.py
```
