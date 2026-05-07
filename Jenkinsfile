pipeline {
    agent any

    environment {
        APP_DIR = '/home/ubuntu/apps/flask-app'
        VENV_DIR = '/home/ubuntu/apps/flask-app/venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/aakash-1004/flask-mongo-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    # Install from workspace where requirements.txt was just pulled
                    ${VENV_DIR}/bin/pip install -r ${WORKSPACE}/requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    # Copy new code to app directory
                    sudo -u ubuntu cp -r ${WORKSPACE}/* ${APP_DIR}/
                    # Restart app
                    sudo -u ubuntu /usr/lib/node_modules/pm2/bin/pm2 restart flask-app
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask deployment successful'
        }
        failure {
            echo 'Flask deployment failed'
        }
    }
}
