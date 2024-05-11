pipeline {
    environment {
        registry = "anusha172000/mlops_assignment_anusha_husnain" 
        registryCredential = 'docker-hub-credentials' 
        dockerImage = ''
    }
    agent any
    stages {
        stage('Get Dockerfile from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/revolutionarybukhari/CICD-1' 
            }
        }
        stage('Build Docker image') {
            steps {
                script {
                    dockerImage = docker.build(registry + ":$BUILD_NUMBER")
                }
            }
        }
        stage('Push Docker image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Send Email Notification') {
            when {
                branch 'main' 
            }
            steps {
                script {
                    // Sending email notification upon successful build
                    emailext (
                        to: 'i200626@nu.edu.pk', 
                        subject: "Merging to  main branch ",
                        body: "successful merge to the main branch was .",
                        attachLog: true,
                        mimeType: 'text/plain'
                    )
                }
            }
        }
    }
}
