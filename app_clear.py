from flask import Flask, render_template
from flask_sock import Sock
import json
from great_things import audio

app = Flask(__name__)
app.config["SOCK_SERVER_OPTIONS"] = {"ping_interval": 25}

sock = Sock(app)


def log(msg, *args):
    print(msg, *args)


@app.route("/twiml", methods=["GET", "POST"])
def index():
    return render_template("streams.xml")


@sock.route("/")
def echo(ws):
    log("Connection Accepted!")

    played_tone = False
    count = 0
    stream_sid = ""

    while True:
        message = ws.receive()

        if message is None:
            log("No message receieved!")
            continue

        data = json.loads(message)

        if data["event"] == "connected":
            log(message)

        if data["event"] == "start":
            stream_sid = data["streamSid"]
            log(message)

        if data["event"] == "dtmf":
            log(message)

        if data["event"] == "media":
            if int(data["media"]["chunk"]) >= 100 and int(data["media"]["chunk"]) <= 200 and not played_tone:
                send_to_twilio = {
                    "event": "media",
                    "streamSid": stream_sid,
                    "media": {"payload": audio},
                }
                mark_message = {
                    "event": "mark",
                    "streamSid": stream_sid,
                    "mark": {
                        "name": "This is my mark message!"
                    }
                }
                ws.send(json.dumps(send_to_twilio))
                log(f"Sending the following message to Twilio: {mark_message}")
                ws.send(json.dumps(mark_message))
                played_tone = True
                continue
            
            #try to send clear to stop the previous message midway
            if int(data["media"]["chunk"]) >= 201 and played_tone:
                clear_message = {
                    "event": "clear",
                    "streamSid": stream_sid,
                }
                log(f"Sending the following message to Twilio: {clear_message}")
                ws.send(json.dumps(clear_message))
                played_tone = False
                continue

            log(message)
        
        if data["event"] == "mark":
            log("We got a mark message back from Twilio!")
            log(message)

        if data["event"] == "stop":
            log(message)
            ws.close()
            break


if __name__ == "__main__":
    app.run()
