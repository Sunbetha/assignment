pipeline {
    agent any

    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'jenkins-latest', url: 'https://github.com/Sunbetha/assignment.git'
            }
        }

        stage('Install') {
            steps {
                    sh '''
                    pip install -r requirements.txt
                    '''
            }
        }

        stage('Test') {
            steps {
                    sh '''
                    cd deploy
                    python3 -m tests.test_server
                    '''
            }
        }

        stage('Build') {
            steps {
                    sh '''
                    docker build -t sunbeth/assignment:${BUILD_NUMBER} .
                    '''
            }
        }
        stage('Login') {
             steps {
                 sh '''
                 echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                 '''
            }
        }

        stage('push'){
            steps {
                    sh '''
                    docker push sunbeth/assignment:${BUILD_NUMBER}
                    '''
            }
        }
    }

    post {
        success {
            // Notify or perform additional actions on successful build and deployment
            echo 'Build and deployment successful!'
        }
        failure {
            // Notify or perform additional actions on build or deployment failure
            echo 'Build or deployment failed!'
        }
    }
}
