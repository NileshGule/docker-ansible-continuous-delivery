### 1 - Build development image


### 2 - Create application requirements file
> `source venv/bin/activate`

>`pip freeze > requirements.txt`

### 3 - Test development image
> `docker build -t todobackend-dev -f docker/dev/Dockerfile .`

As part of housekeeping, add venv folder to dockerignore file

### 4 - Reduce testing time
Create docker volume to share the pip cache
>``
### 5 - Use different test settings
