# Simple Web App For Finding Blood Doner

Follow following steps to make sure the app runs:

1. It is recommended to create the new environment for each project:(So, create and activate your environment)
> virtualenv newenv

> source newenv/bin/activate

2. Do install all the requirements.
 > pip install -m requirements.txt

3. Make sure you check the Database section on settings.py. And add the configuration for the system:
``` 
DATABASES = {
  'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER':'created_user',
        'PASSWORD':'your_password',
        'PORT':'5432',
        'HOST':'localhost'
    }
}
```

4. Then make sure you migrate all the models to the database configured on the settings.py.
> python manage.py makemigrations

> python manage.py migrate

5. Then finally run the server.
> python manage.py runserver
