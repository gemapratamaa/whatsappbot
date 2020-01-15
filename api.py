import requests
import json
import random
from PIL import Image
import webbrowser

dogUrl = "https://dog.ceo/api/breeds/image/random"
response = requests.get(dogUrl)
jsoned = json.loads(response.text)
randomPicUrl = jsoned['message']
msg.media(randomPicUrl)
webbrowser.open(randomPicUrl)
#randomPic.show() 
#pic = json.loads(r)
#print(r)