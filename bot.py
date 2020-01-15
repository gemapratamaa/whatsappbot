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
    print(counter)
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    if counter == 0:
        #print("masuk")
        greeting_msg = f'''Hi! I'm a WhatsApp chat bot made by Gema. For now I can only do these things:
        1. Give you a quote by typing "quote"
        2. Give you a picture of a dog by typing "dog"
        '''
        msg.body(greeting_msg)
        counter += 1
        return str(resp)
    
    responded = False

    #if incoming_msg == '1':
     #   guess_number_game()
    
    if incoming_msg.isnumeric():
        msg.body('You have typed a number {}.\n\n'.format(incoming_msg))
        msg.body('After {} is {}, and before {} is {}.'.format(
            incoming_msg, 
            str(int(incoming_msg) + 1), 
            incoming_msg,
            str(int(incoming_msg) - 1)
            )
        )
        #msg.body("{} dikali 2 = {}".format(incoming_msg, int(incoming_msg) * 2))
        responded = True
        return str(resp)

    if incoming_msg == 'quote':
        url = "https://type.fit/api/quotes"
        result = json.loads(requests.get(url).text)
        randomQuote = random.choice(result)['text']
        msg.body(randomQuote)
        responded = True

        return str(resp)

    if incoming_msg == 'dog':
        dogUrl = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(dogUrl)
        jsoned = json.loads(response.text)
        randomPicUrl = jsoned['message']
        msg.media(randomPicUrl)

        return str(resp)
    

    if incoming_msg.isalpha():
        if len(incoming_msg) == 1:
            response = "You have typed a letter {}.".format(incoming_msg)
            msg.body(response)
            responded = True
        else:
            response = "You have typed an alphabetic string with {} characters: {}".format(len(incoming_msg), incoming_msg)
            msg.body(response)
            responded = True

        return str(resp)
    
    if incoming_msg.isalnum() and len(incoming_msg) > 1:
        response = "You have typed an alphanumeric characters with {} characters: {}".format(len(incoming_msg), incoming_msg)
        msg.body(response)
        responded = True

        return str(resp)

    if not incoming_msg.isalnum():
        response = "You have typed a non alphanumeric string: {}".format(incoming_msg)
        msg.body(response)
        responded = True

        return str(resp)
    
    return str(resp)

def main():
   print("Main")

def randomQuote():
    url = "https://type.fit/api/quotes"
    result = json.loads(requests.get(url).text)
    randomQuote = random.choice(result)['text']
    msg.body(randomQuote)

def guess_number_game():
    print("masuk")
    high = 0
    low = 0
    win = 0
    number = random.randint(1, 10)
    userNum = int(request.values.get('Body', '').lower())
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("Please guess a number between 1 and 10: ")

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


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
    #main()

