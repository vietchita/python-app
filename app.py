from flask import Flask
import os
import random
from datetime import datetime

app = Flask(__name__)

MIN = int(os.environ.get('MIN', 1))
MAX = int(os.environ.get('MAX', 100))

@app.route('/random')
def random_number():
    return str(random.randint(MIN, MAX)) + '\n'

@app.route('/status')
def status():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Hello from python app at {current_time}  v1 \n v2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

