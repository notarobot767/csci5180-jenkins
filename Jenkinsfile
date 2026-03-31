pipeline {
    agent any 
    stages {
        stage('Stage 1: Update Packages') {
            steps {
                echo 'Updating Debian packages...'
                sh '''
                    sudo apt-get update
                    sudo apt-get upgrade -y
                    sudo apt-get install -y \
                        python3 \
                        python3-ncclient \
                        python3-pandas \
                        python3-netaddr \
                        python3-prettytable \
                        pylint
                '''
            }
        }
        
        stage('Stage 2: Checking and fixing violations') {
            steps {
                echo 'Building...'
                sh 'pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" netman_netconf_obj2.py > pylint.log || true'
                recordIssues(
                    tool: pyLint(pattern: 'pylint.log'),
                    qualityGates: [
                        [threshold: 10, type: 'TOTAL', criticality: 'FAILURE']
                    ],
                    failGeneally: true 
                )
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