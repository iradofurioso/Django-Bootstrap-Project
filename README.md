# PyDBP - Django Bootstrap Project

![Django 2.1.7](http://img.shields.io/badge/Django-2.1.7-0C4B33.svg) [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) [![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)


PyDBP is a personalized project template for Django 2.1.7 specially designed for websites and online applications with a bunch of other goodies. PyDBP is lightweight with folder structure tweaks following the best practices.

PyDBP is best suited for medium-sized and bigger apps that use JQuery and Bootstrap for frontend. Some highlights:

  - Python 3.7.2
  - Tested on MacOS Mojave and Apache
  - Django 2.1.7
  - PIP 19.0.3
  - Deployed in production - KingHost 

# Creating your Project

The description below provides the necessary steps to get this template working smoothly on your machine. 

## Setup virtual environment
  
First things first! Make sure you have the virtual environment working before starting any new project. 

```sh
$ mkdir myproject
$ cd myproject
$ python3 -m venv .virtualenvs
$ . .virtualenvs/bin/activate
```

Please note:
  - The folder name is just for the sake of an example.
  - Configure this folder in your Apache virtualhost or NGINX. 
  - ".virtualenvs" is the name I chose you can keep it or create a new one. 
  - The last bash command has a single dot "." just an alias to the command "source".

## Install Django 

Install the latest Django version. Be aware this template was tested under version 2.1.7

```sh
$ pip install django
```

## Create a new Django app

Now it's to start the project with PyDBP template. 

* **Template link** [https://github.com/tresloukadu/Django-Bootstrap-Project/archive/master.zip](https://github.com/tresloukadu/Django-Bootstrap-Project/archive/master.zip)

```sh
$ django-admin startproject  --template https://github.com/tresloukadu/Django-Bootstrap-Project/archive/master.zip  --extension=py,md,html,txt apps_wsgi
```

Please note:

I decided to start the project and create the files in a folder named "apps_wsgi" just because it seems more Apache friendly. However you can pick any other name. Another possibility is in the case you already created and is inside the app folder so last argument (folder name) you can change for a dot (.). 

## Import requirements

After creating the project it is necessary to import the requirements listed in the "Requirements" folder. Inside the application folder (the same with manage.py) run the following command:

```sh
$ pip install -r Requirements/requirements.txt
```

## Do the migration 

Now you can migrate Django default tables. Please, make sure you added the database configuration options in your settings.py insde PyDBP!

```sh
$ python manage.py migrate
```

## Creating superuser

Run the following command to create the administrator user:

```sh
$ python manage.py createsuperuser
```

## Framework configuration 

The above actions is the necessary commands to get application running. However, if you try to access in your web browser you will face some errors. This is due to missing information in settings.py and Boot.py. Be aware that this template loads the Decouple module so you don't necessarily need to edit setting.py but only the .env file. First of all change the name of the file:

```sh
$ mv .env.example .env
```
Then edit the .env file with your project configuration information. 

**.env**
```txt
ALLOWED_HOSTS=.mydomain.com
SECRET_KEY=<YOUR SECRETE KEY>
DEBUG=True
LANGUAGE_CODE=pt-br
TIME_ZONE=America/Sao_Paulo
```

**Boot.py**
```py
site.addsitedir('<ABSOLUT PATH TO PROJECT ROOT>/.virtualenvs/lib/python3.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('<ABSOLUT PATH TO PROJECT ROOT>/apps_wsgi')
sys.path.append('<ABSOLUT PATH TO PROJECT ROOT>/apps_wsgi/PyDBP')
```

## Run webserver

In case you don't have Apache you can run Django custom server.

```sh
$ python manage.py runserver
```

However if you have Apache, your have to add your project and application path in your WSGI configuration and restart Apache. The configuration of Apache is not covered here, but maybe in the future. 


# Todos

 - Write MORE Tests

License
----

MIT


**Free Software, Hell Yeah!**