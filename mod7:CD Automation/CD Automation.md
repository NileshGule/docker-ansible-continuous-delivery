# Test, Build & Release Automation

## GNU Make build system
Add makefile

Add the relative path to docker/dev folders docker-compose YAML file

Test the make command
> `make test`

Add tasks for other workflows related to the test stage

Similarly add the tasks for build & releases stages to the make file

## Automate the workflow

---
# Workflow infrastructure

## Github
Create 5 repositories in github
1 - docker-ansible
2 - todobackend
3 - todo-backend-base
4 - todobackend-client
5 - todobackend-specs

## Docker Hub
Create repository for storing docker images
todobackend

login to dockerhub from commandline
> `docker login`

push the image to dockerhub
> `docker push nileshgule/todobackend-client`
