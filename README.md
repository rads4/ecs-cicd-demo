# ECS CI/CD Automation with Jenkins

This project demonstrates a simple CI/CD pipeline that automates the redeployment of an AWS ECS application using Jenkins. The pipeline is triggered automatically when changes are pushed to the GitHub repository.

The setup uses a Jenkins controller–agent architecture where build jobs run only on the Jenkins agent (slave) with limited IAM permissions. The agent executes a Python script that uses the AWS SDK (boto3) to trigger ECS service redeployments.

## Architecture Overview

GitHub → Jenkins Webhook → Jenkins Controller → Jenkins Agent → Python (boto3) → AWS ECS

1. A code change is pushed to the GitHub repository.
2. GitHub sends a webhook event to Jenkins.
3. Jenkins triggers the pipeline automatically.
4. The pipeline runs on the Jenkins agent node.
5. The agent executes a Python script that calls the AWS ECS API.
6. ECS performs a new deployment of the frontend and backend services.

## Repository Structure

```
ecs-cicd-demo/
│
├── Jenkinsfile
├── deploy_ecs.py
└── README.md
```

## Jenkins Pipeline

The pipeline runs on the Jenkins agent and performs the following:

1. Pull the latest code from GitHub.
2. Execute the Python deployment script.
3. Trigger a forced ECS service redeployment.

Example pipeline stage:

```
pipeline {
    agent { label 'ecs-slave' }

    stages {
        stage('Deploy ECS') {
            steps {
                sh 'python3 deploy_ecs.py'
            }
        }
    }
}
```

## Python Deployment Script

The deployment script uses boto3 to call the ECS `update_service` API and trigger a new deployment.

Example logic:

```
ecs.update_service(
    cluster=cluster_name,
    service=service_name,
    forceNewDeployment=True
)
```

This forces ECS to start new tasks and replace the running ones.

## Features

* Automated ECS deployment using Jenkins pipeline
* GitHub webhook based push trigger
* Jenkins controller–agent architecture
* Deployment automation using Python and boto3
* Least privilege IAM role for Jenkins agent

## AWS Services Used

* Amazon ECS
* Amazon EC2
* IAM
* Jenkins
* GitHub

## How the Deployment Works

When code is pushed to the repository:

1. GitHub webhook triggers Jenkins.
2. Jenkins runs the pipeline on the agent node.
3. The Python script calls the ECS API.
4. ECS performs a rolling deployment of the services.

This ensures application services are redeployed automatically without manual intervention.
