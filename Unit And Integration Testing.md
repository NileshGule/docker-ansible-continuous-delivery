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
> brew install homebrew/versions/mysql56

## Configure integration tests

## Improve test output
