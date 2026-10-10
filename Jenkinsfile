pipeline{
    agent any 
    
    stages{
        stage('Checkout'){
            steps{
                git branch:'master',url:'https://github.com/wadawadagitulsi/pytest_add.git'
            }
        }
        stage('Run python'){
            steps{
                bat 'python add.py 50 100'
            }
        }
    stage('Run Tests'){
            steps{
                bat 'python -m pytest -v'
            }
        }        
    }
}