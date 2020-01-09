from flask import Flask,request,jsonify
import requests
import json

app = Flask(__name__) 

# bot token id
token = "969230639:AAE_Iyythzr_zvHFpNbA8XnoTEi2BjmqaI4"

# base url for telegram api
telegram_url = f"https://api.telegram.org/bot{token}/"

@app.route('/msg',methods=['GET','POST']) 
def messages():
    if request.method == "POST":

        # formatting post data into dict
        data = {
            "chat_id":request.values.get('chat_id'),
            "text":request.values.get('text')
        }

        # requesting telergram api with formatted postd data
        # Bot will send message to dedicated user based on chat_id
        # Based on chat_id, dedicated user will recieve message from bot
        req = requests.post(telegram_url+"sendMessage",data=data)

        # converting response data into json
        response = req.json()

        print(response)
        
        # defining variables from formatted json
        # response = response['result']
        # message_id = response['message_id']
        # message = response['text']
        # date = response['date']
        # chat_id = response['chat']['id']
        # chat_user_first_name = response['chat']['first_name']
        # chat_user_last_name = response['chat']['last_name']
        # chat_username = response['chat']['username']
        # chat_type = response['chat']['type']

        # returns response from telegram api for sending message to the user
        return jsonify(response)
    elif request.method == "GET":

        # requesting telegram api for latest updates in the bot
        req = requests.post(telegram_url+"getUpdates")

        # converting response into json
        response = req.json()

        # returns response from telegram api for requesting latest updates
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True) 
