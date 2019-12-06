pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python --version'
                sh 'printenv'
                sh 'python -m py_compile config.py'
            }
        }
    }
}
