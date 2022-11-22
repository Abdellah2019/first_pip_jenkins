pipeline {
  agent any
  stages {
    stage('build') {
      agent any
      steps {
        sh 'echo "I like CI CD"'
        sh 'python --version'
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