# Bi-directional Media Streams Example

This Python Flask app is based on the code from Twilio's media-streams repo, specifically the [Python basic example.](https://github.com/twilio/media-streams/tree/master/python/basic)

There are 2 main differences with this code compared to Twilio's:

1. Twilio's example is uni-directional vs. this example is bi-directional
2. This example is based on the more modern [flask-sock](https://github.com/miguelgrinberg/flask-sock) library in comparison to [flask-sockets](https://github.com/heroku-python/flask-sockets) which is deprecated.

## Installation

1. Create a venv by running `python3 -m venv venv && source venv/bin/activate`
2. Run `pip install -r requirements.txt`
3. Run the app by running `python app.py`
4. By default, the app will be bound to localhost on port 5000
5. To expose the app to the internet, you can use ngrok by running the command `ngrok http 5000`
6. In the Twilio Console, use the ngrok URL as your Voice URL, appending `/twiml` for the phone number you would like to use. For example - https://123456789.ngrok.io/twiml
7. You will also need to replace the WSS URL in the [streams.xml](templates/streams.xml) file, for example - wss://123456789.ngrok.io/

## About the app

Included with the app (app.py) is a mulaw encoded raw (headerless) audio file that has been encoded using base64. When the call first connects, the app will recieve 100 chunks of audio from the caller, once it reached 100 chunks, the app will send audio back to Twilio. You will hear the full audio - "When you use Twilio and media stream you can achieve great things"

app_clear.py extend the above app by exploring how to sending [clear message](https://www.twilio.com/docs/voice/twiml/stream#message-clear-to-twilio) to interrupt the audio that has been sent. You will hear partial audio - "When you use Twilio and media stream". Run the app by running python app_clear.py
