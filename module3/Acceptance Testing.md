## Acceptance testing module related steps & commands

### 1 - Initial Setup
Deactivate from virtual environment
> `deactivate`

#### Install node.js
> `brew install node.js`

#### Create directory for functional tests
> `mkdir todobackend-specs`

> `cd todobackend-specs`

#### Initialize a git repo
> `git init`

#### Create .gitignore file and add node_modules to it
> `touch .gitignore`

> `npm init`

After successful intialization, install various node packages
> `npm install bluebird chai chai-as-promised mocha superagent superagent-promise mocha-jenkins-reporter --save`

Save flag is used to add the packages as dependencies in the package.json file

### 2 - Writing acceptance tests
Refer to https://github.com/NileshGule/docker-ansible-continuous-delivery/commit/5b6329b8f5def3658cfd586590f249c71c914062 for more details

### Running Acceptance tests
> `source venv/bin/activate'

#### Run tests
> `python manage.py runserver --settings=todobackend.settings.test`

Migrations error is shown, run the migrations before running the tests

> `python manage.py migrate --settings=todobackend.settings.test`

Rerun the server
> `python manage.py runserver --settings=todobackend.settings.test`
