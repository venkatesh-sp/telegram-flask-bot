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
        return jsonify(response)
    elif request.method == "GET":

        # requesting telegram api for latest updates in the bot
        req = requests.post(telegram_url+"getUpdates")

        # converting response into json
        response = req.json()

        # returns response from telegram api for requesting latest updates
        return jsonify(response)
@app.route('/setwebhook',methods=['GET','POST'])
def setWebhook():
    if request.method == "GET":
        req = requests.post(telegram_url+"setWebhook",params={'url':"https://telegram-flask-bot.herokuapp.com/msg"})
        return jsonify(req.json())

@app.route('/getwebhook',methods=['GET','POST'])
def getWebhook():
    if request.method == "GET":
        req = requests.post(telegram_url+"getWebhookInfo")
        return jsonify(req.json())


if __name__ == '__main__':
    app.run(debug=True) 
