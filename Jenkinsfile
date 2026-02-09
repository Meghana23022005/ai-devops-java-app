pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

        stage('AI Code Analysis') {
            steps {
                withSonarQubeEnv('SonarQube-Local') {
                    bat 'mvn sonar:sonar -Dsonar.projectKey=ai-devops-java-app'
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t ai-devops-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f ai-devops-container || exit 0'
                bat 'docker run -d -p 8082:8081 --name ai-devops-container ai-devops-app'
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed – capturing logs and invoking MCP AI Agent'
			script {
				writeFile(
					file: 'jenkins.log',
					text: currentBuild.rawBuild.getLog(1000).join('\n')
            )
        }
        bat '''
        "C:\\Users\\hskav\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" mcp_agent.py jenkins.log
        '''
        }
    }
}
