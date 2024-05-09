pipeline {
    agent any
    
    environment {
        DOCKER_CREDENTIALS_ID = '38627808-a1ee-4df7-9831-b3cea1abaa28'
        IMAGE_TAG = "anusha3172000/diabetes_prediction_app:${env.BUILD_ID}"
    }
    
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build IMAGE_TAG
                }
            }
        }
        
        stage('Publish') {
            when {
                branch 'master' // Only trigger this stage when changes are merged into master
            }
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                            docker.image(IMAGE_TAG).push()
                        }
                    }
                }
            }
        }
    }
    
    post {
        success {
            emailext(
                to: 'anushazubair2000@gmail.com', // Specify the email address of the admin
                subject: "Success: Deployment #${env.BUILD_NUMBER}",
                body: "The deployment of build #${env.BUILD_NUMBER} to Docker Hub was successful.",
                attachLog: true
            )
        }
    }
}
