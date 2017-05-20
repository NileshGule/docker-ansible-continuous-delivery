# Enhance the workflow

## Dangling images & volumes
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

## Make the workflow self contained

## Producing test reports

## Handle errors

## Ensure consistency

## Tag & Publish

## Convert files to use Docker Compose V2 Specification
