pipeline {
    agent { docker { image 'python:3.6.8' } }
    stages {
        stage('run_python_script') {
            steps {
                sh 'python --version'
            }
        }
    }
}
