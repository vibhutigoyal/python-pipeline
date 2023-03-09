pipeline {
	agent any
	stages {
		stage ("pull scm python test") {
			steps {
				git branch: 'python', url: 'https://github.com/vibhutigoyal/python-pipeline.git'
				}
			}
		stage ("Build") {
			steps {
				sh 'python3 -V'
				sh 'python3 cp.py'
				}
			}
		stage ("Test") {
			steps {
				sh 'python3 test.py'
				}
			}
		}
	}
