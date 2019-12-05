pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'printenv'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Hello World"'
                retry(3) {
                    sh 'python --version'
                }
                sh 'printenv'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Fail!"; exit 1'
                ssh './gradlew check'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
            archiveArtifacts artifacts: 'build/libs/**/*.jar', fingerprint: true
            junit 'build/reports/**/*.xml'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}