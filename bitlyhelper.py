import json
from urllib.request import urlopen

TOKEN='1fc0219c4f3695677bd70494a39184514c6e8e28'
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:
	def shorten_url(self, longurl):
		try:
			url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
			response = urlopen(url).read()
			jr = json.loads(response)
			return jr['data']['url']
		except Exception as e:
			print(e)