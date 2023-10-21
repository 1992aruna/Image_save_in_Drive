from flask import Flask, request, jsonify
from bot import Bot
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import traceback

""" 
Uncomment the below line for production  for pythonanywhere production , Replace <loc> with location of folder in pythonanywhere
And Comment  the line : load_dotenv() 
and  vice vera for localhost
"""
#load_dotenv(os.path.join("/home/<loc>", '.env'))

load_dotenv()

API_URL=os.getenv("API_URL")
ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
load_dotenv()


MONGO_URI=os.getenv("MONGO_URI")
API_URL=os.getenv("API_URL")
ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
PAY_USERNAME=os.getenv("PAY_USERNAME")
PAY_PASSWORD=os.getenv("PAY_PASSWORD")



app= Flask(__name__)


UPLOAD_FOLDER = 'static/data/images'

app.secret_key = b'_m9y2L*79xQ8z\n\xec]/'

app.config["MONGO_URI"] = MONGO_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mongo = PyMongo(app)

db = mongo.db

@app.errorhandler(500)
def internal_server_error(e):
    # Log the error details to a file or other logging system
    traceback.print_exc()

    # You can customize the error response sent to the client
    error_response = "Internal Server Error"
    
    # You can also include additional error details if needed
    error_response += "\n" + str(e)
    
    # Return the error response and 500 status code
    return error_response, 500


@app.route('/', methods=['GET'])
def home():
    return "Bot Live 3.0"

@app.route('/webhook', methods=['POST', 'GET'])
def hook():
    if request.method == 'POST':
        data=request.json
        #print(data)
        if "created" in data:
            number=data['waId']
            bot = Bot(db, data,number,  API_URL, ACCESS_TOKEN, app.config["UPLOAD_FOLDER"], PAY_USERNAME, PAY_PASSWORD)
            return bot.processing()
    return "Processing..."

if __name__ == '__main__':
    app.run(debug=True) 