pipeline { 
    agent any
    environment {
        IMAGE_NAME = "ghcr.io/gomezf2/ci-pipeline-demo"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
    }
}
