import requests
import inflection
from bs4 import BeautifulSoup

#get data from the site
r = requests.get('http://www.dailysmarty.com/topics/python')
centinel = 'data-turbolinks="false" href="' 
enlaces_manual = []
enlaces_with_beauti = []


def get_links_list():
	start_index = 0
	final_index = 0
	max_value_index = r.text.rfind(centinel)
	
	while start_index < max_value_index:	
		start_index = r.text[final_index:].find(centinel) + final_index
		final_index = start_index + r.text[start_index:].index('">')
		enlace = r.text[start_index:final_index].lstrip(centinel).split('/')[-1]	
		enlaces_manual.append(enlace)
	
	#print(enlaces_manual)


def get_links_list_with_beautifulshop():
	soup = BeautifulSoup(r.text, 'html.parser')
	links_wrapper = soup.find_all("h2")

	for a_link in links_wrapper:
		str_link = str(a_link).partition('">')[0]
		str_link = str(str_link).split('/')[-1]
		enlaces_with_beauti.append(str_link)
		
	#print(enlaces_with_beauti)


def prepare_link_list(links):
	for link in links:
		print(inflection.titleize(link))


#main
#get_links_list()
#prepare_link_list(enlaces_manual)
get_links_list_with_beautifulshop()
prepare_link_list(enlaces_with_beauti)