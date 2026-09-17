pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

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

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh '''
                        ${SCANNER_HOME}/bin/sonar-scanner
                    '''
                }
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

        stage('Trivy Security Scan') {
            steps {
                sh '''
                    trivy image \
                      --severity HIGH,CRITICAL \
                      --exit-code 1 \
                      devops-sre-backend:${BUILD_NUMBER}
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
