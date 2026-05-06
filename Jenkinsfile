pipeline {
    agent any

    environment {
        APP_DIR = '/home/ubuntu/apps/flask-app'
        VENV_DIR = '/home/ubuntu/apps/flask-app/venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull latest code from GitHub into Jenkins workspace
                git branch: 'main',
                    url: 'https://github.com/aakash-1004/flask-mongo-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python packages using the app's virtualenv
                sh '''
                    cd ${APP_DIR}
                    ${VENV_DIR}/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                // Copy updated code to app directory and restart via PM2
                sh '''
                    cp -r ${WORKSPACE}/* ${APP_DIR}/
                    pm2 restart flask-app
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
