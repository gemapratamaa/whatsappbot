import requests
import json
import urllib
#userInput = input("input:")

foxUrl = "https://randomfox.ca/floof/"
response = requests.get(dogUrl)
jsoned = json.loads(response.text)
randomPic = jsoned['image']
print(randomPic)