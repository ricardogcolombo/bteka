pipeline {
  agent { docker { image 'python:3.7.0' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python bteka-tests.py'
      }   
    }
  }
}