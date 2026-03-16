pipeline {

    agent { label 'ecs-slave' }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/rads4/ecs-cicd-demo.git'
            }
        }

        stage('Deploy ECS') {
            steps {
                sh 'python3 deploy_ecs.py'
            }
        }

    }
}
