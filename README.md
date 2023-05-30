#Bi-directional Media Streams Example

This Python Flask app is based on the code from Twilio's media-streams repo, specifically the [Python basic example.](https://github.com/twilio/media-streams/tree/master/python/basic)

There are 2 main differences with this code compared to Twilio's:

1. Twilio's example is uni-directional vs. this example is bi-directional
2. This example is based on the more modern [flask-sock](https://github.com/miguelgrinberg/flask-sock) library in comparison to [flask-sockets](https://github.com/heroku-python/flask-sockets) which is deprecated.

##Installation

1. Create a venv by running `python3 -m venv venv && source venv/bin/activate`
2. Run `pip install -r requirements.txt`
3. Run the app by running `python app.py`

##About the app

Included with the app is a mulaw encoded raw (headerless) audio file that has been encoded using base64. When the call first connects, the app will recieve 100 chunks of audio from the caller, once it reached 100 chunks, the app will send audio back to Twilio.
