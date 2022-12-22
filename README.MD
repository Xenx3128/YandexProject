# YaCoder install & set up
YaCoder is a social network for the people who are interested in olimpiad programming and algorithms

## Setup
download python on [official site](https://www.python.org/)

clone repo:

```sh
$ git clone https://github.com/Xenx3128/YandexProject/
$ cd YandexProject
```

### set environment variables
create .env file and declare DEBUG=True or DEBUG=False in it



### Create a virtual environment activate it:
```sh
$ python -m venv venv
```
on linux
```sh
source venv/bin/activate
```
windows
```sh
venv/scripts/activate
```
install 
```sh
pip install -r requirements.txt
```
then 
```sh
$ cd project
```

### apply migrations
```sh
python manage.py migrate
```

### create superuser
```sh
python manage.py createsuperuser
```

### run server
```sh
$ python manage.py runserver 8000
```
now server runs on 127.0.0.1:8000
admin panel you can visit in /admin/