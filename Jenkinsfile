pipeline {
    agent any

    environment {
        // Ensure this username is correct
        DOCKERHUB_USER = "vodnalasanthosh47"    
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/vodnalasanthosh47/CICD-Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Modified for Windows: Use 'bat', backward slashes, and direct script calls
                bat '''
                    python -m venv venv
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\pip.exe install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Modified for Windows: Set PYTHONPATH via 'set' and call pytest via python module
                bat '''
                    set PYTHONPATH=.
                    venv\\Scripts\\python.exe -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                // Use double quotes "..." so Groovy interpolates ${DOCKERHUB_USER} before running the command
                bat "docker build -t ${DOCKERHUB_USER}/myapp:latest ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
                    // Windows Batch Syntax:
                    // 1. Use @echo off or @echo to prevent printing the command (hides password in logs)
                    // 2. Use %DOCKER_PASS% for the environment variable in Batch
                    bat '@echo %DOCKER_PASS% | docker login -u ${DOCKERHUB_USER} --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat "docker push ${DOCKERHUB_USER}/myapp:latest"
            }
        }

        stage('Verify Image') {
            steps {
                bat 'docker images'
            }
        }
    }
}