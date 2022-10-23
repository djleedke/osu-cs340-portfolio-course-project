# Fine Midwestern Dining

## Useful Links

[OSU Flask Guide](https://github.com/osu-cs340-ecampus/flask-starter-app)

## Python Commands

Create virtual environment:
```
$ python3 -m venv venv
```

Start virtual environment:
```
$ source venv/bin/activate
```

Install required modules:
```
$ pip3 install -r requirements.txt
```

Start localhost (Development):
```
$ python3 app.py
```

## Server Commands

Start gunicorn (Production):
```
$ gunicorn -b 0.0.0.0:<PORT NUMBER> -D app:app
```

Kill gunicorn:
```
$ pkill -u <osu_id> gunicorn
```