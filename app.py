from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os
import random
import json
import urllib.request

app = Flask(__name__)
counter = 0

@app.route('/bot', methods=['POST'])
def bot():
    global counter
    
    #incomingMsg = request.values.get('Body', '').lower()
    incomingMsg = request.values.get('Body', '').lower().split(' ')
    resp = MessagingResponse()
    msg = resp.message()
    
    if counter == 0:
        greeting_msg = f'''Hi! I'm a WhatsApp chat bot made by Gema. For now I can only do these things:
        1. Give you a quote by typing "quote"
        2. Give you a picture of a dog by typing "dog"
        3. Give you a picture of a random meme by typing "meme"
        4. Give you a picture of a random cat by typing "cat"
        5. Give you a random fact by typing "fact"
        6. Give you a (messy) live score of NBA by typing "nba"

        1. Give you a random picture of an animal (available animals: dog, cat, fox) by typing the respective animal name.

        The source code can be found in https://github.com/gemapratamaa/whatsappbot

        This bot is still in production! You may encounter some bugs
        '''
        msg.media("https://realestatekawagoe.com/wp-content/uploads/2019/10/1412350.jpg")
        msg.body(greeting_msg)

        counter += 1
        return str(resp)
    
    responded = False
    
    if len(incomingMsg) == 1:
        if incomingMsg[0] == 'quote':
            url = "https://type.fit/api/quotes"
            result = json.loads(requests.get(url).text)
            randomQuote = random.choice(result)['text']
            msg.body(randomQuote)
            responded = True
            return str(resp)

        elif incomingMsg[0] == 'dog':
            dogUrl = "https://dog.ceo/api/breeds/image/random"
            response = requests.get(dogUrl)
            jsoned = json.loads(response.text)
            randomPic = jsoned['message']
            msg.media(randomPic)
            return str(resp)

        elif incomingMsg[0] == 'fox':
            foxUrl = "https://randomfox.ca/floof/"
            response = requests.get(dogUrl)
            jsoned = json.loads(response.text)
            randomPic = jsoned['image']
            msg.media(randomPic)
            return str(resp)

        elif incomingMsg[0] == 'meme':
            memeUrl = "https://some-random-api.ml/meme"
            response = requests.get(memeUrl)
            jsoned = json.loads(response.text)
            randomMeme = jsoned['image']
            msg.media(randomMeme)
            return str(resp)
        
        elif incomingMsg[0] == 'cat':
            catUrl = "https://api.thecatapi.com/v1/images/search"
            response = requests.get(catUrl)
            jsoned = json.loads(response.text)
            randomCatPic = jsoned[0]['url']
            msg.media(randomCatPic)
            return str(resp)
        
        elif incomingMsg[0] == 'fact':
            factUrl = "https://uselessfacts.jsph.pl/random.json?language=en"
            response = requests.get(factUrl)
            jsoned = json.loads(response.text)
            randomFact = jsoned['text']
            msg.body(randomFact)
            msg.body("\r\n\r\nFrom: {}".format(jsoned['source']))
            return str(resp)
        
        elif incomingMsg[0] == 'nba':
            url = "http://api.isportsapi.com/sport/basketball/livescores?api_key=VNhjOMjbs2kQmk9Z"
            f = urllib.request.urlopen(url)
            content = f.read()
            decoded = content.decode('utf-8')
            jsoned = json.loads(decoded)

            for k in jsoned['data']:
                if k['leagueName'] == 'NBA':
                    remainingQuarterTime = k['quarterRemainTime']
                    homeTeam = k['homeName']
                    awayTeam = k['awayName']
                    homeScore = k['homeScore']
                    awayScore = k['awayScore']
                    msg.body("{} (home) vs {} (away)".format(homeTeam, awayTeam))
                    msg.body("Current score: {} - {}".format(homeScore, awayScore))
                    msg.body("Time remaining in quarter: {}".format(remainingQuarterTime)) 
            
            return str(resp)

        elif incomingMsg == 'game':
            msg.body("Please guess a number between 1 and 10: ")
            print("masuk")
            high = 0
            low = 0
            win = 0
            number = random.randint(1, 10)
            userNum = int(request.values.get('Body', '').lower())

            while userNum != number:
                msg.body("Try again: ")
                if userNum > number:
                    msg.body("Too high, try again.")
                    high += 1
                elif userNum == number:
                    msg.body("You got it correct! Congratulations!")
                    win += 1
                    break
                else:
                    msg.body("Too low, try again.")
                    low += 1
            
            msg.body(("Number of times too high: ", high))
            msg.body(("Number of times too low: ", low))
        else:
            msg.body("Couldn't recognize that command :/ Please try again")

        return str(resp)

    elif len(incomingMsg) == 2:
        pass

    
@app.route('/')
def index():
    return "<h1>Welcome to Gema's server !!</h1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
    
"""
    if incomingMsg.isnumeric():
        msg.body('You have typed a number {}.\n\n'.format(incomingMsg))
        msg.body('After {} is {}, and before {} is {}.'.format(
            incomingMsg, 
            str(int(incomingMsg) + 1), 
            incomingMsg,
            str(int(incomingMsg) - 1)
            )
        )
        responded = True
        return str(resp)
    """