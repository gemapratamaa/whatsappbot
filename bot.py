from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os
import random
import json

app = Flask(__name__)
counter = 0

@app.route('/bot', methods=['POST'])
def bot():
    global counter
    
    incomingMsg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    if counter == 0:
        greeting_msg = f'''Hi! I'm a WhatsApp chat bot made by Gema. For now I can only do these things:
        1. Give you a quote by typing "quote"
        2. Give you a picture of a dog by typing "dog"
        3. Give you a picture of a random meme by typing "meme"
        '''
        msg.body(greeting_msg)
        counter += 1
        return str(resp)
    
    responded = False
    
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

    if incomingMsg == 'quote':
        url = "https://type.fit/api/quotes"
        result = json.loads(requests.get(url).text)
        randomQuote = random.choice(result)['text']
        msg.body(randomQuote)
        responded = True

        return str(resp)

    elif incomingMsg == 'dog':
        dogUrl = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(dogUrl)
        jsoned = json.loads(response.text)
        randomPic = jsoned['message']
        msg.media(randomPic)

        return str(resp)

    elif incomingMsg == 'meme':
        memeUrl = "https://meme-api.glitch.me/light"
        response = requests.get(memeUrl)
        jsoned = json.loads(response.text)
        randomMeme = jsoned['meme']
        msg.media(randomMeme)

        return str(resp)
    
    elif incomingMsg == 'cat':
        catUrl = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(catUrl)
        jsoned = json.loads(response.text)
        randomCatPic = jsoned[0]['url']
        msg.media(randomCatPic)

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

def main():
   print("Main")

def randomQuote():
    url = "https://type.fit/api/quotes"
    result = json.loads(requests.get(url).text)
    randomQuote = random.choice(result)['text']
    msg.body(randomQuote)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)


    """
    if incomingMsg.isalpha():
        if len(incomingMsg) == 1:
            response = "You have typed a letter {}.".format(incomingMsg)
            msg.body(response)
            responded = True
        else:
            response = "You have typed an alphabetic string with {} characters: {}".format(len(incomingMsg), incomingMsg)
            msg.body(response)
            responded = True

        return str(resp)
    
    if incomingMsg.isalnum() and len(incomingMsg) > 1:
        response = "You have typed an alphanumeric characters with {} characters: {}".format(len(incomingMsg), incomingMsg)
        msg.body(response)
        responded = True

        return str(resp)

    if not incomingMsg.isalnum():
        response = "You have typed a non alphanumeric string: {}".format(incomingMsg)
        msg.body(response)
        responded = True

        return str(resp)
    """