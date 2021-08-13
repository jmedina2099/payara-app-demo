import os
import time
import requests
import subprocess
import sys

from dopost import DoPost
from doall import DoAll
from clean import DoClean

class Script():

	url1 = 'http://localhost:8080/app-demo/data/all'
	url2 = 'http://localhost:8080/app-demo/data'
	url3 = 'http://localhost:8080/app-demo/data/1'
	appName = 'payara-app-demo'
	versionName = 'v15'
	imageName = appName + ':' + versionName

	def __init__(self,clean):
		print('===============================================================================')
		print('=======================         BEGIN         =================================')
		print('===============================================================================')
		self.compile_war_file()
		#self.run_sonarqube()
		self.build_docker_image()
		self.run_docker_image()
		self.show_docker_container()
		self.show_docker_images()
		self.waiting()
		self.test_get_all()
		self.test_post_all()
		self.test_get_1()
		self.test_get_all()
		self.do_clean(clean)
		self.show_container_id()
		self.show_image_id()
		print('===============================================================================')
		print('=======================         END           =================================')
		print('===============================================================================')

	def compile_war_file(self):
		print('*********************** COMPILING WAR         *********************************')
		os.system('mvn package')

	def run_sonarqube(self):
		print('*********************** RUN SONAR             *********************************')
		os.system('mvn sonar:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.login=d563a7e59818d6abbb6426a317b81cb77e8cb98a')

	def build_docker_image(self):
		print('*********************** BUILDING DOCKER IMAGE *********************************')
		os.system('docker build -f src/main/docker/Dockerfile -t ' + self.imageName + ' .')

	def run_docker_image(self):
		print('*********************** RUNNING DOCKER IMAGE  *********************************')
		os.system('docker run -d -p 8080:8080 -p 8181:8181 -p 4848:4848 -p 8009:8009 ' + self.imageName )

	def show_docker_container(self):
		print('*********************** SHOWING CONTAINERS    *********************************')
		os.system('docker ps')

	def show_docker_images(self):
		print('*********************** SHOWING IMAGES        *********************************')
		os.system('docker images')

	def waiting(self):
		print('*********************** WAITING..             *********************************')
		time.sleep(15)

	def test_get_all(self):
		print('*********************** TESTING ALL (GET)     *********************************')
		DoAll().do_curl_get(self.url1)

	def test_post_all(self):
		print('*********************** TESTING (POST)        *********************************')
		DoPost().do_post(self.url2)

	def test_get_1(self):
		print('*********************** TESTING (GET)         *********************************')
		DoAll().do_curl_get(self.url3)

	def do_clean(self,clean):
		if clean == 1:
			DoClean().do_auto_clean();

	def show_container_id(self):
		print("CONTAINER ID")
		os.system('docker ps -q')

	def show_image_id(self):
		print("IMAGE ID")
		os.system('docker images -q')

value = 0
argsn = len(sys.argv)
if argsn > 1:
	value = int(sys.argv[1])
Script(value)