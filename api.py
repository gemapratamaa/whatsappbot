import requests
import json
import random
from PIL import Image
import webbrowser
"""
dogUrl = "https://dog.ceo/api/breeds/image/random"
response = requests.get(dogUrl)
jsoned = json.loads(response.text)
randomPicUrl = jsoned['message']
msg.media(randomPicUrl)
webbrowser.open(randomPicUrl)
#randomPic.show() 
#pic = json.loads(r)
#print(r)
"""

jokeUrl = "http://api.icndb.com/jokes/random/"
response = requests.get(jokeUrl)
jsoned = json.loads(response.text)
print(jsoned)

randomJoke = jsoned['value']['joke']
print(randomJoke)