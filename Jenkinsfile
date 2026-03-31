pipeline {
    agent any
    triggers {
        // run every night at 2:00 AM
        cron('0 2 * * *')
    }
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
                echo 'checking for violations...'
                sh 'pylint netman_netconf_obj2.py > pylint.log || true'
                recordIssues(
                    tool: pyLint(pattern: 'pylint.log'),
                    qualityGates: [
                        [
                            threshold: 5,
                            type: 'TOTAL',
                            criticality: 'FAILURE'
                        ]
                    ]
                )
                
            }
        }

        stage('Stage 3: Running the application') {
            steps {
                echo 'Executing netman_netconf_obj2.py'
                sh 'python3 netman_netconf_obj2.py'
            }
        }

        stage('Stage 4: Unit test') {
            steps {
                echo 'Executing test_netman.py'
                sh 'python3 test_netman.py'
            }
        }
    }
    post {
        always {
            emailext (
                subject: "NetMan Build ${currentBuild.fullDisplayName}: ${currentBuild.currentResult}",
                body: """<h3>Build Status: ${currentBuild.currentResult}</h3>
                         <p>The Jenkins pipeline for <b>netman_netconf_obj2.py</b> has finished.</p>
                         <p>Check the console output here: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                to: 'nrogrydziak@gmail.com',
                from: 'jenkins@netman.io'
            )
        }
    }
}