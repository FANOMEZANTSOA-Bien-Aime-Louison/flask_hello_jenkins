pipeline {
  agent {
    kubernetes {
      label 'jenkins-agent'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.12
    command:
    - cat
    tty: true
"""
    }
  }
  
  triggers {
    pollSCM('* * * *')
  }
  
  stages {
    stage('Test') {
      steps {
        container('python') {
          dir('flask_app') {
            sh 'pip install -r requirements.txt'
            sh 'python test.py'
          }
        }
      }
    }
  }
}