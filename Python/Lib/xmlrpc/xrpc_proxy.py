#!/usr/bin/env python3
# xrpc_proxy.py - a `xmlrpc.client` example with proxy support
#                 extracted from official python's manuals

import os
import base64
import pprint
import urllib.parse
import http.client
import xmlrpc.client


class ProxiedTransport(xmlrpc.client.Transport):
	"""A xmlrpc transport to pass-throught a http proxy"""

	def set_proxy(self, proxy):
		"""Assign the proxy settings"""
		if proxy.startswith('http://'):
			proxy = urllib.parse.urlparse(proxy).netloc

		auth, host = urllib.parse.splituser(proxy)
		self._proxy_host = host

		if auth:
			auth = urllib.parse.unquote_to_bytes(auth)
			auth = base64.encodebytes(auth).decode("utf-8")
			auth = "".join(auth.split())
			self._proxy_headers = {
				'Proxy-Authorization': 'Basic ' + auth,
			}
		else:
			self._proxy_headers = {}
	
	def send_request(self, host, handler, request_body, verbose):
		"""Open connection and send the given request"""
		selector = 'https://{0}{1}'.format(host, handler)
		print(host, handler, request_body, self.user_agent)

		connection = http.client.HTTPConnection(self._proxy_host)
		connection.set_debuglevel(1)
		connection.putrequest('POST', selector, skip_host=True)

		connection.putheader('Host', host)
		connection.putheader('Content-Type', 'text/xml')
		connection.putheader('User-Agent', self.user_agent)
		for h in self._proxy_headers:
			connection.putheader(h, self._proxy_headers[h])
		connection.endheaders()

		return connection


if __name__ == '__main__':
	transport = None
	http_proxy = os.environ.get('http_proxy')
	if http_proxy:
		transport = ProxiedTransport()
		transport.set_proxy(http_proxy)
	pypi_endpoint = 'http://pypi.python.org/pypi'
	pypi_server = xmlrpc.client.ServerProxy(pypi_endpoint, transport, verbose=True)
	pprint.pprint(pypi_server.release_urls('roundup', '1.4.10'))

# EOF
