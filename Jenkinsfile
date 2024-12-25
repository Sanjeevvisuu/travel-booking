pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub') // Environment variable for Docker Hub credentials
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Sanjeevvisuu/travel-booking.git'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo 'Building the Django application as a Docker image...'
                    sh '''
                    # Ensure that the Jenkins user can access Docker (optional if sudo is configured)
                        docker-compose build
                    '''
                }
            }
        }

        stage('Docker Image Push') {
            steps {
                script {
                    echo 'Pushing application to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                        # Log in to Docker Hub
                        echo "$DOCKER_PASSWORD" |  docker login -u "$DOCKER_USERNAME" --password-stdin
                        # Tag and push the image to Docker Hub
                           docker tag  django_travel $DOCKER_USERNAME/travel_app:latest
                           docker push $DOCKER_USERNAME/travel_app:latest
                        '''
                    }
                    echo 'Pushed application to Docker Hub.'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...' // Cleanup after build completes, regardless of success or failure
        }
        success {
            echo 'Pipeline succeeded!'
            
            
            emailext(
                subject: "Jenkins Pipeline Succeeded: Travel Booking App - Build #${BUILD_NUMBER}",
                body: """The Jenkins pipeline for the Travel Booking App has completed successfully.
                    Build Information:
                    - Build Number: ${BUILD_NUMBER}
                    - Build Status: ${BUILD_STATUS}
                    - Build URL: ${BUILD_URL}
                    - Console Output:
                    ${buildLog}
                    Please check the Jenkins console output for details.""",
                to: "sanjeevvisuu@gmail.com"
            )
        }
        failure {
            echo 'Pipeline failed!'
            
            emailext(
                subject: "Jenkins Pipeline Failed: Travel Booking App - Build #${BUILD_NUMBER}",
                body: """The Jenkins pipeline for the Travel Booking App has failed.
                    Build Information:
                    - Build Number: ${BUILD_NUMBER}
                    - Build Status: ${BUILD_STATUS}
                    - Build URL: ${BUILD_URL}
                    - Console Output:
                    ${buildLog}
                    Please check the Jenkins console output for details.""",
                to: "sanjeevvisuu@gmail.com"
            )
        }
    }
}
