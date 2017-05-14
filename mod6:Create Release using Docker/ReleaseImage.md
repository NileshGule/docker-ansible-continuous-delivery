# Create release environment
## Create application release settings
Create `release.py` setitgns file under the `src/todobackend/settings` folder

Set debug mode to false
Add allowed host environment setting

Add MySQL database connection settings
Add the static root & media root variable to be read from the environment settings

Update the `setup.py` file to include uwsgi package as part of install_requires variable

Rebuild the images
> `docker-compose kill`

Remove images
> `docker-compose rm -f`

Run docker compose build to rebuild the images
> `docker-compose build`

> `docker-compose up agent`

> `docker-compose up test`

> `docker-compose up builder`

---
## Create release image
Create `Dockerfile` under the `docker/release` folder

Base the image on nileshgule/todobackend-base:latest version

Copy artifacts from /wheelhouse directory

---
## Describe release environment
Create the environment in a docker compose file

Add ngnix config file named `todobackend.conf`

---
# Bootstrap release environment
Run the docker compose
> `docker-compose build`

> `docker-compose up agent`

> `docker-compose up app`

Add libpython2.7 depepndency to the base image

rebuild base image and the release environment

---
# Run acceptance test

### Bootstrap the application
add app service as the link

> `docker-compose up nginx`

Copy the static content by running the command to collect static files
> `docker-compose run --rm app manage.py collectstatic --noinput`

> `docker-compose up nginx`

Run the table migrations
>`docker-compose run --rm app manage.py migrate --noinput`

### Run acceptance tests
Create test service
Create Dockerfile in the todobackend-specs

Create .dockerignore file to exclude `node_modules` folder from being copied to the image

Build the docker image
> `docker build -t nileshgule/todobackend-specs .`

Create a test service in the docker-compose file for release environment

Run acceptance test
clean up the release environment
> `docker-compose kill`

> `docker-compose rm -f`

> `docker-compose build`

> `docker-compose up agent`

> `docker-compose run --rm app manage.py collectstatic --noinput`

>`docker-compose run --rm app manage.py migrate --noinput`

> `docker-compose up test`

Publish the release image
