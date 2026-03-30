pipeline {
    agent any 
    stages {
        stage('Update Packages') {
            steps {
                echo 'Updating Debian packages...'
                // Use sudo only if the Jenkins user has passwordless sudo rights
                sh 'sudo apt-get update && sudo apt-get upgrade -y'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
    }
}