import requests
import inflection

r = requests.get('http://www.dailysmarty.com/topics/python')

#print(r.text)

tx = "/posts/steps-for-building-a-flask-api-application-with-python-3".lstrip("/popts/")
print(tx)
tx = tx.split('-')
print(tx)

tx_2 = ""
for noun in tx:
	tx_2 += ' ' + noun
print(tx_2)

print(inflection.camelize(tx_2, uppercase_first_letter=True))
print(tx_2)