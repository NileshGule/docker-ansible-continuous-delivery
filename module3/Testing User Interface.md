## Testing the user Interface
### 1 - Installing the Todobackend client
clone the repository for todobackend client application
> `git clone https://github.com/jmenga/todobackend-client.git`

> `cd todobackend-client`

> `npm install`

got an error saying grunt command not found.

Install grunt-cli
>`npm install -g grunt-cli`

Rerun npm install after successful grunt installation

source venv & start the todobackend
> `source venv/bin/activate`

>`cd src`

>`python manage runserver --settings=todobackend.settings.test`

Start the client
>`node app.js`

### 2 - Verifying the user Interface
#### Navigate to the url
> `http://localhost:3000`
