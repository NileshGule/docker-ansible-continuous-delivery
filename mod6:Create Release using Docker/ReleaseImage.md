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
