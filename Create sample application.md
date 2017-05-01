#Create sample application module

##Create todobackend web service application

### Install Django framework
pip install django==1.9

### Initiate a todobackend project using django admin command
django-admin startproject todobackend

cd todobackend

### create a src folder & move manage.py + todobackend directory to src

mkdir src
mv manage.py src
mv todobackend/ src

#commit the changes to reposiroty
git add -A

git commit -a -m "Initial commit"

### Ensure virtualenv packagae is installed
pip install virtualenv

### Create virtual environemnt using virtualenv command
virtualenv venv

### Activate the virtual environment by sourcing bin/activate script
source venv/bin/activate

### Install all required packages inside the virtual environment
pip install pip --upgrade

### Install Django into virtual environment
pip install django==1.9

### Install Djangorest framework
pip install djangorestframework==3.3


### Install Django CORS headers for cross origin headers support
pip install django-cors-headers==1.1

cd src

### Start the application using startapp command
python manage.py startapp todo

### Update setting.py to include the additional apps & libraries
### Update the contents of models.py to define the TodoItem model
