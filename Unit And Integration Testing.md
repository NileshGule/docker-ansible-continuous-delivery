# Unit and Integration Testing
## Creating tests
Create helper function which creates todo items
Create different test methods and classes for testing features like creating todo item, deleting todo item, updating todo item and delete all todo items
Refer to https://github.com/NileshGule/docker-ansible-continuous-delivery/commit/9a913a08ad5deb80a1aaee8d77489c14e0f213e3 for more details

Run tests using command
> python manage.py test

## Refactoring settings
Create environment related settings
Create 'settings' folder under Django root folder
Create __init.py__ file
Copy settings.py and rename to base.py
Update manage.py default setting from todobackend.settings to todobackend.settings.base
Update the wsgi.py default setting from todobackend.settings to todobackend.settings.base

Add additional settings
Create test.py in settings folder
override the MySQL database default settings

### Install MYSQL
> 'brew install homebrew/versions/mysql56'
The command to install specific version of MySQL 5.6 did not work.

The source for latest version was compiled using
> `brew install mysql --build-from-source`

Verify that the installation was successful by running the command
> `mysql.server start`

Configure password
> 'mysql_secure_configuration'

after setting up different options, login to server
> 'mysql -u root -p'

Once the root password is entered, mysql prompt should appear

### Create todobackend database
> `CREATE DATABASE todobackend`

### Grant required previllages
> `GRANT ALL PRIVILEGES ON *.* TO 'todo1'@'localhost' identified by  'password'`

### Exit mysql prompt
> `quit`

### Install Mysql-python package
> `sudo pip install mysql-python`

### Run tests using new settings
Option 1 - Set DJango settings module environment variable
> `export DJANGO_SETTINGS_MODULE=todonackend.settings.test`

Option 2 - using settings flag for manage.py command
> `python manage.py test --settings=todobackend.settings.test`

## Configure integration tests

## Improve test output
