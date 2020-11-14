## Set up project on the local machine
In order to start project, you need to clone it. I will be doing it using `https://`

```
git clone https://github.com/t2elzeth/ontoto
cd ontoto
```

Create your venv
```
python3 -m venv env
. env/bin/activate

pip install -r requirements.txt
```

Make migrations and create super user
```
./manage.py makemigrations && ./manage.py migrate
./manage.py createsuperuser --email='' --username='admin'
```

Run server
```
./manage.py runserver
```
