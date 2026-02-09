from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "BuildXAI is Live!"

# මේ පේළිය අනිවාර්යයෙන්ම තියෙන්න ඕනේ
if __name__ == "__main__":
    app.run()