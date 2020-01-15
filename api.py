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

catUrl = "https://api.thecatapi.com/v1/images/search"
response = requests.get(catUrl)
jsoned = json.loads(response.text)

print(jsoned[0]['url'])