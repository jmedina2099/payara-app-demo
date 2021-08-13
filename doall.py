import os
import sys

url = 'http://localhost:8080/app-demo/data/all'

class DoAll:

	def __init__(self):
		if sys.argv[0] == 'doall.py':
			self.do_curl_get(url)

	def do_curl_get(self,url):
		print('GET '+url)
		os.system('curl '+url)
		print('')

DoAll()
