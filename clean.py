import os
import argparse
import subprocess
import sys

class DoClean():

	def __init__(self):
		if sys.argv[0] == 'clean.py':
			argsn = len(sys.argv)
			if argsn == 2:
				self.do_auto_clean()
			else:
				self.do_clean_args()

	def do_clean_args(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("container", type=str, help="clean a docker container")
		parser.add_argument("image", type=str, help="clean a docker image")
		args = parser.parse_args()
		container = args.container
		image = args.image
		self.do_clean(container,image)

	def do_auto_clean(self):
		result = subprocess.run(['docker', 'ps', '-q'], stdout=subprocess.PIPE)
		container = result.stdout.decode('utf-8')
		result = subprocess.run(['docker', 'images', '-q'], stdout=subprocess.PIPE)
		image = result.stdout.decode('utf-8')
		self.do_clean(container,image)

	def do_clean(self,container,image):
		print('*********************** STOPPING CONTAINER')
		os.system('docker stop '+container)
		print('*********************** DELETING CONTAINER')
		os.system('docker rm '+container)
		print('*********************** DELETING IMAGE')
		os.system('docker rmi '+image)
		print('*********************** CLEANING TARGET')
		os.system('mvn clean')

DoClean()