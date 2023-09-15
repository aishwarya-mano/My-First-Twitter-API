from flask import Flask, request, jsonify
from flask_cors import CORS

import tweepy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/create", methods=['POST'])
def create_tweet():
    req = request.json
    tweet_text = req['text']

    client = tweepy.Client(bearer_token, api_key,
                           api_key_secret, access_token, access_token_secret)
    try:
        response = client.create_tweet(text=tweet_text)
        print(response)
        return jsonify(isError=False,
                       message="Success",
                       statusCode=200,
                       data=response)
    except Exception as msg:
        val = 'Failed';
        if len(msg.api_messages) > 0:
            val = msg.api_messages[0];
        return jsonify(isError=True,
                       message=val,
                       statusCode=500,
                       data={})

@app.route("/delete/<tweet_id>", methods=['DELETE'])
def delete_tweet(tweet_id):
    client = tweepy.Client(bearer_token, api_key,
                           api_key_secret, access_token, access_token_secret)
    try:
        response = client.delete_tweet(id=tweet_id)
        print(response)
        return jsonify(isError=False,
                       message="Success",
                       statusCode=200,
                       data=response)
    except:
        return jsonify(isError=True,
                       message="Failed",
                       statusCode=500,
                       data={})
