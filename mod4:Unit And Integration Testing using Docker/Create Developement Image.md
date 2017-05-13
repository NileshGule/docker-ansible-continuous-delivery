### 1 - Build development image


### 2 - Create application requirements file
> `source venv/bin/activate`

>`pip freeze > requirements.txt`

### 3 - Test development image
> `docker build -t todobackend-dev -f docker/dev/Dockerfile .`

As part of housekeeping, add venv folder to dockerignore file

### 4 - Reduce testing time
Create docker volume to share the pip cache
>`docker run -v /tmp/cache:/cache --entrypoint true --name cache todobackend-dev`

Run container again by atatching the volume container
> `time docker run --rm --volumes-from cache todobackend-dev`

Run tests with test configuration
>`docker run --rm -e DJANGO_SETTINGS_MODULE=todobackend.settings.test --volumes-from cache todobackend-dev`

### 5 - Use different test settings
#### Create docker compose file

#### Run tests usig Docker compose
>`docker-compose up test`

>`docker-compose ps`

>`docker-compose logs db`

#### Wait for dependent services to Initialize
Create ansible playbook

Kill Images
>`docker-compose kill`

>`docker-compose rm -f`

Verify that the probe is working fine
>`docker-compose up agent`

Run docker compose test which runs all the tests successfully
>`docker-compose up test`

Run docker compose builder to build wheels packages
> `docker-compose up builder`

Navigate to `todobackend` directory and check the contents of target folder
> `ls -l target/*`
