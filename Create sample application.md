#Create sample application module

####Create course root folder
mkdir cd-docker-ansible

### Create Todobackend Web service
#### Initial Setup
Check Python is installed on Mac Machine
>python --version

>Update version of pip easy_install pip
>> If this fails try > sudo easy_install pip

### Install Django framework
pip install django==1.9

If this fails, try with sudo
> sudo easy_install django==1.9

### Initiate a todobackend project using django admin command
django-admin startproject todobackend

cd todobackend

### create a src folder & move manage.py + todobackend directory to src

mkdir src
mv manage.py src
mv todobackend/ src

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

### Create todobackend project using django admin utility
> django-admin startproject todobackend

Child todobackend is the Django root folder

#### Resturucture the layout for CD
>cd todobackend
> mkdir src
> mv manage.py src
> mv todobackend/ src

### Install Djangorest framework
> pip install djangorestframework==3.3

### Install Django CORS headers for cross origin headers support
> pip install django-cors-headers==1.1

cd src

### Start the application using startapp command
>python manage.py startapp todo

#### Create models

#### Create serializers

#### Create Views

#### Configure routing

#### Test drive the application













### Update setting.py to include the additional apps & libraries
### Update the contents of models.py to define the TodoItem model
