from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "BuildXAI is Live and Working!"

app_handle = app