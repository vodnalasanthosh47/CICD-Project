pipeline {
    agent any

    environment {
        IMAGE = "prathamchawdhry/ci-cd-demo2:jenkins"
        VENV = ".venv"
        PYTHON = "/usr/bin/python3" 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.\\venv\\Scripts\\python.exe -m pip install --upgrade pip'
                
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\python.exe test_app.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${DOCKERHUB_USER}/myapp:latest ."
            }
        }
    }
}