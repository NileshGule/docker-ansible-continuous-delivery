# Enhance the workflow

## Dangling images & volumes
---
Update makefile to remove dangling images during the clean target execution

Run the clean command
> `make clean`

Add LABEL to the base image and rebuild the image
> `docker build -t nileshgule/todobackend-base`

Commit the changes to github repo

Rebuild the test & release images
> `make test`

> `make build`

> `make release`

> `make clean`

Add -v flag to docker-compose rm command to remove the dangling volumes

Manually remove the dangling volumes by running command
>`docker volume rm $(docker volume ls -f dangling=true -q)`

Run the make test command
> `make test`

Run the make clean command
> `make clean`

## Improve user feedback
---
Add colourful messages to the output of make file to indicate the progress

## Make the workflow self contained
---
Add the copy command to ansible image to copy the probe.yml file

Rebuild the image
> `docker build -t nileshgule/ansible .`

Commit the changes to github repo

Modify the docker-compose in todobackend dev
 - Update the agent service by removing the volume mapping
 - Add the command to execute the probe.yml playbook from the /ansible working directory
 - Modify the builder service by replacing volume mapping with docker copy command
 - Modify the makefile to copy the artifacts using docker copy command

 Modify the docker-compose in todobackend release folder
 - Modify the agent service by removing volume maping & replacing with command invocation
 - Remove the volume mapping for todobackend.conf file in the nginx service
 - create a dockerfile from nginx image

 run the workflow
 > `make test`

 > `make build`

 > `make release`

## Producing test reports
---
Copy the test results from containers back to the docker client
run the workflow
> `make test`

> `make build`

> `make release`

As part of housekeeping, update gitignore file to exclude reports & target folder
Ignore the reports folder in the dockerignore file

## Handle errors
---
Use the docker rm approach to remove containers where files are not required to be passed back

Define ISPECT variable to extract the exit code from the docker container
Define CHECK variable to check the value of exit code
Implement a make rule that implements the CHECK variable

Modify the test & build workflow
 - Update test task to do a check after copying the test results
 - Update build task to do a check after the artifacts are created

Modify the release workflow
 - Change the docker compose up agent command to docker compose rm command
 - Check the exit code after copying the test results

Run the workflow again for test, build & release stages

## Ensure consistency
---
Modify the test stage
- Add docker compose pull command at the start of the test stage
- Ensure that the test & cache services are built using the latest image of dev image
- Build the test image with pull flag
- Build the cache image without pull flag

Modify the release stage
- Add docker compose pull command to pull the test image
- Build the App & Webroot services without the pull flag
- build the nginx image with the pull flag

Test out the workflow (test, build, release, clean)

## Tag & Publish
---
### Implement the tag functionality

Add tag target to the Makefile
Configure a make function called foreach
Define DOCKER_REGISRTY & TAG_ARGS variables
Get ImageId of container using approach similar to command substitution
Extract the container id using command substitution

Run the workflow (test, build, release)
Tag the image using command
> `make tag 0.1 latest $(git rev-parse --short HEAD)`

Verify tagging has worked successfully by running the docker images command
> `docker images`

### Implement the buildtag functionality
Add buildtag target to makefile
Define BUILD_TAGS variable
Extract BUILD_TAGS similar to the TAGS operation performed earlier

Tag the images using buildtag command
> `make buildtag 0.1 $(git rev-parse --abbrev-ref HEAD)`

### Publish the release image
Add login logout and publish tasks to makefile
Extract image tags using command substitution into a variable named REPO_EXPR
Test the publish by first setting the environment variables for DOCKER_USER, DOCKER_EMAIL and DOCKER_PASSWORD
> `export DOCKER_USER=nileshgule`

> `export DOCKER_EMAIL=vn_nilesh@yahoo.com`

> `export password=<YOUR PASSWORD>`

Run the login command
> `make login`

Publish the images
> `make publish`

## Convert files to use Docker Compose V2 Specification
---
Add the docker compose V2 file to dev & release environments
Explicitly add the version 2 at the beginning of the file
Modify the dynamically built services (test, builder & cache) to provide build context
Define top level volumes
- Define build as local volume
- Define cache as external volume

Use volumes in services
- Use build & cache volumes in test service
- Use cache volume in builder service
- Remove cache service as it is provided by Docker

Modify the makefile to reflect the changes
- Refer the v2 files for dev & release
- Add a new step to test stage to create cache volume
- Remove reference to the cache volume container service

### Build version 2 of the docker compose specification for release stage
- Add explicit version
- Modify services to use build context syntax
- Add volume for webroot as local volume
- Update app and nginx services to refer to the new webroot volume

### Reconfigure the make file to use release config specification
- Remove the action to build webroot container service
- Use the new docker compose down command which cleans up all resources

Test the workflow (test, build, release)
