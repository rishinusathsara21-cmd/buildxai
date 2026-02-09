from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "BuildXAI is Live!"

@app.route('/api/main')
def main_api():
    return "Hello from BuildXAI API!"

if __name__ == "__main__":
    app.run()