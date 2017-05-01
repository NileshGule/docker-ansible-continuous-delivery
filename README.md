# docker-ansible-continuous-delivery

## Environment preparation
### 1 - Install Docker, Docker Machine and Docker Compose
Install Docker & docker machine using brew

> brew install docker-compose
This installs the dependencies for docker-machine which are docker and docker-compose

Verify that the dependencies are installed automatically
>brew install docker

>brew install docker-machine

### 2 - Install Ansible
Check the version of pip package manager
> pip install pip --upgrade

>pip install ansible --upgrade

#### Install additional packages to interact between Ansible & AWS
#### These are official Python SDK to interact with AWS
> pip install boto boto3

#### Install AWS CLI to interact with AWS from commandline
pip install awscli

### 3 - Install other tools
Git
Sublime Text 2 with Material theame
Tree
