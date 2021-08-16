import requests
import sys

from requests.exceptions import ConnectionError

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
payload = {'name': 'Jorge Alberto Medina Rosas', 'organization': 'Stefanini.'}

class DoPost():

	url = 'http://localhost:8080/app-demo/data'

	def __init__(self):
		if sys.argv[0] == 'dopost.py':
			self.do_post(self.url)

	def do_post(self,url):
		try:
			print('POST '+url)
			prepared = requests.post(url, json=payload, headers=headers)
			self.pretty_print_POST(prepared)
			if prepared.status_code == 201:
				print('OK')
				if sys.argv[0] == 'dopost.py':
					sys.exit(0)
			else:
				print('FAIL')
				if sys.argv[0] == 'dopost.py':
					sys.exit(1)
		except ConnectionError as ValueError:
			print(ValueError)
			print('FAIL')
			if sys.argv[0] == 'dopost.py':
				sys.exit(1)

	def pretty_print_POST(self,req):
		print(req)
		print('{}\n{}\r\n{}\r\n\r\n{}'.format(
			'-----------START-----------',
			'[' + req.reason + '] ' + req.url,
			'\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
			'',
		))

DoPost()