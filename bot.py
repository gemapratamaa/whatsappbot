from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os
import random

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
        greeting_msg = f'''Try typing the number below:
        1. Guessing game: Number
        2. Describe what you typed'
        '''
        msg.body(greeting_msg)
        counter += 1

    responded = False

    if incoming_msg == '1':
        guess_number_game()
    """
    if incoming_msg.isdigit():
        msg.body('You have typed a number {}.\n'.format(incoming_msg))
        msg.body('After {} is {}, and before {} is {}'.format(
            incoming_msg, 
            str(int(incoming_msg) + 1), 
            incoming_msg,
            str(int(incoming_msg) - 1)
            )
        )
        responded = True

    if incoming_msg.isalpha():
        if len(incoming_msg) == 1:
            response = "You have typed a letter {}.".format(incoming_msg)
            msg.body(response)
            responded = True
        else:
            response = "You have typed an alphabetic string with {} characters: {}".format(len(incoming_msg), incoming_msg)
            msg.body(response)
            responded = True
    
    if incoming_msg.isalnum() and len(incoming_msg) > 1:
        response = "You have typed an alphanumeric characters with {} characters: {}".format(incoming_msg)
        msg.body(response)
        responded = True

    if not incoming_msg.isalnum():
        response = "You have typed a non alphanumeric string: {}".format(incoming_msg)
        msg.body(response)
    """
    return str(resp)

def main():
   print("Main")

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

