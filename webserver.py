from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
	return "webserver ON discordbot ON"

def run():
	app.run(host="0.0.0.0",port="8080")

def keepalive():
	t = Thread(target=run)
	t.start()