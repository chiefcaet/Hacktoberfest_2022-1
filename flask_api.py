import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'arpit',
                       'email': 'arpit@gmail.com'})
app.run(debug = True)

