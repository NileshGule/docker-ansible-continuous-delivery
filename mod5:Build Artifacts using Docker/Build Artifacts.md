## 1 Add package metadata to application
Add setup.py file which contains the metadata about the package
Refactor requirements.txt file to add pointer to the setup.py packages
Refactor requirements_test.txt to have editable flag pointing to the setup.py extra packages

## 2 Test and build consistency
Test stage builds dependencies into a build cache.
The builder service uses the cache to build artifacts

## 3 Add a builder service
Modify test.sh to download the pip dependencies into build folder.
Also modify the install command to pick the dependencies from the build folder
Modify the dockerfile to add volume for the build folder
Modify docker compose file to add build volume to the cache service

## 4 Build and publish Python wheels
Clean the environment
> `docker-compose kill`

> `docker-compose rm -f`

> `docker-compose up agent`

> `docker-compose up test`

Clean the environment again as the dev_test image is not rebuilt
> `docker-compose kill`

> `docker-compose rm -f`

Restart the test stage with build command which forces the docker-compose to rebuild the image
> `docker-compose build`

> `docker-compose up agent`

> `docker-compose up test`

Build application artifacts
> `docker-compose up builder`
