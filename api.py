import requests
import json
import urllib
#userInput = input("input:")

catUrl = "https://restcountries.eu/rest/v2/name/indonesia"
response = requests.get(catUrl)
jsoned = json.loads(response.text)
decoded = jsoned.decode('utf-8')
print(decoded)