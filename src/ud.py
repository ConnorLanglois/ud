import json
import tor
from time import sleep
from urllib import request

def post(url, data, headers, handlers):
	opener = request.build_opener(*handlers)
	req = request.Request(url, json.dumps(data).encode(), headers, method='POST')
	res = opener.open(req)

def get_proxy_handler():
	proxy = '127.0.0.1:8118'
	proxies = {
		'http': proxy,
		'https': proxy
	}
	proxy_handler = request.ProxyHandler(proxies)

	return proxy_handler

URL = 'http://api.urbandictionary.com/v0/vote'
DATA = {
	'defid': 0,
	'direction': 'up'
}
HEADERS = {
	'Content-Type': 'application/json; charset=UTF-8',
	'Host': 'api.urbandictionary.com',
	'Origin':' http://www.urbandictionary.com',
	'Referer': 'http://www.urbandictionary.com/define.php?term=',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
HANDLERS = [get_proxy_handler()]

for i in range(1000):
	post(URL, DATA, HEADERS, HANDLERS)
	print('Voted')

	wait = tor.clean()

	print('Sleeping ' + str(wait))
	sleep(wait)
