#CD using Ansible
##Todobackend CloudFormation template

##Ansible Deployment Playbook

- Deploying overview
- Configure Access to AWS
- Create Playbook
- Test Playbook

### Configure Access to AWS
Install AWS CLI
`brew install awscli`

Install Ansible
`brew install ansible`

In the AWS management console generate the key under IAM section for the admin user.

Run the aws configure command
`aws configure`

Create secrets.yml file using ansible-vault command
`ansible-vault create secrets.yml`
awsAnsibleVault

Test the Playbook
`ansible-playbook site.yml --ask-vault-pass`

### Install custom Ansible modules
Create a directory named `library` to store the custom modules
`mkdir library`

`curl -L -o library/aws_ecs_task.py http://bit.ly/1RHcapd`
`curl -L -o library/aws_ecs_taskdefinition.py http://bit.ly/1RHc6pp`
##Continuously Deploying to AWS
