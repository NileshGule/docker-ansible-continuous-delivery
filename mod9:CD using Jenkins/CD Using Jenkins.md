# CD using Jenkins
## Test, Build and Release using Pipeline Plugin
---
### Setup Jenkins Locally
#### Create Jenkins image
Create Jenkins Docker image
Use official Jenkins docker image
Add Docker & Docker compose
Install Ansible & AWS Python client called boto

Create Dockerfile
Add plugins.txt file for Jenkins plugins
Create docker-compose.yml file to define volumes & services

Create docker volume
> `docker volume create --name jenkins_home`

Run docker compose
> `docker-compose up -d`

Run docker-compose logs command to see if there were any errors
> `docker-compose logs`

After the Jenkins image is built successfully browse the localhost to Verify
In this case the local address was 192.168.99.100:8080

#### Configure the workflow
#### Test the Workflow
#### Create self defined workflow
#### Test failures

## Jenkins in a container
---

## Configure and test workflow
---

## Deploy Jenkins to AWS EC2 Container Service using CloudFormation
---

## Github and Docker Hub integration
