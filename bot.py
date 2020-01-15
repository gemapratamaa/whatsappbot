from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import os
import random

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
        
    responded = False
    
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
    
    return str(resp)

"""
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')

        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True

    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        
        msg.body('coba ketik yg laen')
    return str(resp)
"""
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)