pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub') // Environment variable for Docker Hub credentials
    }
    stages {
        // Stage for checking out the source code from the GitHub repository
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Sanjeevvisuu/travel-booking.git'
            }
        }

        // Stage for building the Docker image for the Django application
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

        // Stage for pushing the built Docker image to Docker Hub
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

    // Post-build actions
    post {
        always {
            echo 'Cleaning up workspace...' // Cleanup after build completes, regardless of success or failure
        }
        success {
            echo 'Pipeline succeeded!'
            // Send email on successful build
            emailext(
                subject: "Jenkins Pipeline Succeeded: Travel Booking App",
                body: """The Jenkins pipeline for the Travel Booking App has completed successfully.
                    Build Information:
                    - Build Number: ${BUILD_NUMBER}
                    - Build Status: ${BUILD_STATUS}
                    - Build URL: ${BUILD_URL}
                    Please check the Jenkins console output for details.""",
                to: "sanjeevvisuu@gmail.com"
            )
        }
        failure {
            echo 'Pipeline failed!'
            // Send email on build failure
            emailext(
                subject: "Jenkins Pipeline Failed: Travel Booking App",
                body: """The Jenkins pipeline for the Travel Booking App has failed. Please check the Jenkins console output for details.
                    Build Information:
                    - Build Number: ${BUILD_NUMBER}
                    - Build Status: ${BUILD_STATUS}
                    - Build URL: ${BUILD_URL}
                    Please check the Jenkins console output for details.""",
                to: "sanjeevvisuu@gmail.com"
            )
        }
    }
}
