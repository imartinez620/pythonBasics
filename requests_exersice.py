import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts')

r_list = r.json()['posts']
#pprint.pprint(r_list)
#r.json()
#pprint.pprint(r.json()['posts'][0])
#pprint.pprint(r.json()['posts'][0]['url_for_post'])

for url in r_list:
	if url['url_for_post']:
		print(url['url_for_post'])


