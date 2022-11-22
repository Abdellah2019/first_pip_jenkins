pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo "I like CI CD"'
        mail(subject: 'Resultat Build', body: 'le build est b1 passé', to: 'abdellah.hemed@gmail.com', from: 'cheikhelmoustaphea@gmail.com', charset: 'utf-8')
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