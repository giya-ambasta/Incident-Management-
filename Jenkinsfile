pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "giyaambasta/incident-app:latest"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/giya-ambasta/Incident-Management-.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh "docker push $DOCKER_IMAGE"
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f incident-container || true
                docker rm -f incident-app || true
                docker run -d -p 5000:5000 \
                -e DB_HOST=mysql-db \
                -e DB_PORT=3306 \
                -e DB_USER=pyuser \
                -e DB_PASSWORD=py123 \
                -e DB_NAME=pypro \
                --name incident-container $DOCKER_IMAGE
                '''
            }
        }

    }
}