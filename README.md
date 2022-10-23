# osu-cs340-course-project


## Bash Commands

Start virtual environment:
```
source/bin/activate
```

Start localhost server:
```
python app.py
```

Start gunicorn (Production):
```
gunicorn -b 0.0.0.0:<PORT NUMBER>
```

Kill gunicorn:
```
pkill -u <osu_id> gunicorn
```