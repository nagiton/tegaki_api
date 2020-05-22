import sys
sys.path.append('/home/ubuntu/anaconda3/lib/python3.6/site-packages')
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({"text":"Hello World!!"})

if __name__ == '__main__':
    app.run()