pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    cd backend
                    python3 -m venv test-venv
                    ./test-venv/bin/pip install -r requirements.txt
                    ./test-venv/bin/python -m compileall app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                      -t devops-sre-backend:${BUILD_NUMBER} \
                      backend/
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}
