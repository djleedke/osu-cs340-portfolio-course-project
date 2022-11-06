# Fine Midwestern Dining

## Useful Links
[Fine Midwestern Dining - Deployed](http://flip1.engr.oregonstate.edu:62135/)\
[Database Outline - Google Doc](https://docs.google.com/document/d/1r1YOmKD8Faw_jGJnt9fxkOBgoKmawmMp_ffnnMa_sSY/edit)\
[OSU Flask Guide](https://github.com/osu-cs340-ecampus/flask-starter-app)\
[CS 340 Project Guide](https://canvas.oregonstate.edu/courses/1890458/pages/cs340-project-guide)\
[Bootstrap v5.0 Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

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

## SQL Commands
Login to MariaDB CLI (password last 4 of ONID):
```
mysql -u cs340_<osu_user_id> -h classmysql.engr.oregonstate.edu -p <osu_user_id>
```

Execute a query from a .sql file (in MariaDB CLI):
```
source <file_name.sql>
```

Backup database:
```
mysqldump -u cs340_<osu_user_id> -h classmysql.engr.oregonstate.edu -p <osu_user_id> > backup.sql
```

Foreign key checks:
```
SET FOREIGN_KEY_CHECKS=0; --Turn Off
SET FOREIGN_KEY_CHECKS=1; --Turn On
```