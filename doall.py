import os
import sys
import subprocess

from subprocess import CalledProcessError

class DoAll:

	def __init__(self):
		if sys.argv[0] == 'doall.py':
			argsn = len(sys.argv)
			if argsn > 1:
				url = sys.argv[1]
			else:
				url = 'http://localhost:8080/app-demo/data/all'
			self.do_curl_get(url)

	def do_curl_get(self,url):
		print('');
		print('GET '+url)
		#os.system('curl '+url)
		batcmd = 'curl '+url
		try:
			result = subprocess.check_output(batcmd, shell=True)
			print(result)
			print('OK')
			if sys.argv[0] == 'doall.py':
				sys.exit(0)
		except CalledProcessError as ValueError:
			print(ValueError)
			print('FAIL')
			if sys.argv[0] == 'doall.py':
				sys.exit(1)

DoAll()
