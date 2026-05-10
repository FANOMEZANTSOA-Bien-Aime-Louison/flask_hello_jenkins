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

  - name: docker
    image: docker:25
    command:
    - cat
    tty: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock

  - name: kubectl
    image: bitnami/kubectl:latest
    command:
    - cat
    tty: true

  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
    }
  }

  options {
    disableConcurrentBuilds()
  }

  triggers {
    pollSCM('*/5 * * * *')
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

    stage('Build and Push') {
      steps {
        container('docker') {
          dir('flask_app') {
            sh 'docker build -t localhost:4000/flask_hello:latest .'
            sh 'docker push localhost:4000/flask_hello:latest'
          }
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        container('kubectl') {
          dir('flask_app') {
            sh 'kubectl apply -f kubernetes/deployment.yml'
            sh 'kubectl apply -f kubernetes/service.yml'
          }
        }
      }
    }
  }
}