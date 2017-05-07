#Create sample application module

####Create course root folder
> `mkdir cd-docker-ansible`

### Create Todobackend Web service
#### 1. Initial Setup
Check Python is installed on Mac Machine
> `python --version`

>Update version of pip `easy_install pip`
>> If this fails try > `sudo easy_install pip`

### Install Django framework
> pip install django==1.9

If this fails, try with sudo
> sudo easy_install django==1.9

### Initiate a todobackend project using django admin command
> django-admin startproject todobackend

Child todobackend is the Django root folder

> cd todobackend

### create a src folder & move manage.py + todobackend directory to src
#### Restructure the layout for CD

> mkdir src
> mv manage.py src
> mv todobackend/ src

## Virtual environment creation
Install Virtualenv package
> sudo pip install virtualenv

Create viirtual environment using virtualenv command
> virtualenv venv

### Activate the virtual environment by sourcing bin/activate script
> source venv/bin/activate

### Install all required packages inside the virtual environment
> pip install pip --upgrade

### Install Django into virtual environment
> pip install django==1.9

### Install Djangorest framework
> pip install djangorestframework==3.3

### Install Django CORS headers for cross origin headers support
> pip install django-cors-headers==1.1

cd src

### Start the application using startapp command
> python manage.py startapp todo



#### To stop the virtual environment
> deactivate

#### 2. Create models
### Create TodoItem as a model with 4 properties title, completed, url and order

### Create schema for TodoItem using built in ORM, todo1 is the application name in below command
> python manage.py makemigrations todo1

### Apply migrations
> python manage.py migrate

### By default Django stores the data in the local SQLite databse

#### 3. Create serializers
###

#### Create Views
Update views.py file with required settings & functions

#### Configure routing
Update urls.py file with required settings and functions

#### Test drive the application
> python manage.py runserver

If everything is fine, then the application should be accessible using Django rest API on http://localhost:8000 url












### Update setting.py to include the additional apps & libraries
### Update the contents of models.py to define the TodoItem model
