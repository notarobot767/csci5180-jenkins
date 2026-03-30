pipeline {
    agent any 
    stages {
        stage('Stage 1: Update Packages') {
            steps {
                echo 'Updating Debian packages...'
                sh 'sudo apt-get update && sudo apt-get upgrade -y'
            }
        }
        
        stage('Stage 2: Checking and fixing violations') {
            steps {
                echo 'Building...'
            }
        }

        stage('Stage 3: Running the application') {
            steps {
                echo 'Building...'
            }
        }

        stage('Stage 4: Unit test') {
            steps {
                echo 'Building...'
            }
        }
    }
}