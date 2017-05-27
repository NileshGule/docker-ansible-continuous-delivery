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
Create a new job
Note: Not all the plugins were installed successfully at this stage. Manually installed the plugins using Jenkins Manage Plugins options
May2017 - Jenkins Nilesh

Configure the pipeline with following Groovy script
`node {
    git 'https://github.com/nileshgule/todobackend.git'

  try {
      stage 'Run unit/integration tests'
      sh 'make test'

      stage 'Build application artifacts'
      sh 'make build'

      stage 'Create release environemnt and run acceptance tests'
      sh 'make release'

      stage 'Tag and publish the release image'
      sh "make tag latest \$(git rev-parse --short HEAD) \$(git tag --points-at HEAD)"
      sh "make buildtag master \$(git tag --points-at HEAD)"
      withEnv(["DOCKER_USER=${DOCKER_USER}",
               "DOCKER_PASSWORD=${DOCKER_PASSWORD}",
               "DOCKER_EMAIL=${DOCKER_EMAIL}"]) {
                   sh "make login"
      }

      sh 'make publish'



  }
  finally {
      stage 'collect test reports'
      step([$class: 'JUnitResultArchiver', testResults: '**/reports/*.xml'])

      stage 'Clean up'
      sh 'make clean'
      sh 'make logout'
  }
}`

#### Test the Workflow
After successful publish, check the dockerhub image for todobackend is updated
#### Create self defined workflow
Create Jenkinsfile to make the workflow self describing
Add the groovy script & modify the git statement to checkout scm
Modify the Jenkins job
#### Test failures

## Jenkins in a container
Build the image to be pushed to dockerhub
> `docker build -t nileshgule/jenkins:latest .`

Build the image which will be pushed to Amazon EC2 container
> `docker build --build-arg DOCKER_ENGINE=1.9.1 -t nileshgule/jenkins:ecs`

Push the image to dockerhub
---
> `docker push nileshgule/jenkins`

## Configure and test workflow
---

## Deploy Jenkins to AWS EC2 Container Service using CloudFormation
---
Create AWS account if it doesn't exist
Remember to create free tier account & set the billing alerts
Create new user using Identity & Access management link for admin activities
Assign Administrative policy template to this
Create keypair
Move the private key to ssh folder
> `mv ~/Downloads/admin.pem.txt ~/.ssh/admin.pem.txt`

Give rights only to the owner to modify the key file
> `chmod 600 ~/.ssh/admin.pem.txt`

###Reveiew the VPC infrastructure

### Create CloudFormation template
Create stack.json file in the docker-jenkins folder

## Github and Docker Hub integration
