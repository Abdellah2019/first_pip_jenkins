pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python --version'
        sh 'echo "I like CI CD"'
      }
    }

    stage('Test') {
      steps {
        sh 'echo "Test project"'
        sh '''echo "Test part 1 ..."
echo "Test part 2 ..."
echo "Test part 3 ..."
'''
      }
    }

    stage('Deploy') {
      steps {
        sh 'echo "Start deployment .."'
      }
    }

  }
}