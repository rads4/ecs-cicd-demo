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
