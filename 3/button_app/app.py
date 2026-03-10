from flask import Flask, render_template, redirect
import requests
import os

app = Flask(__name__)

CLOCK_APP_URL = os.environ.get('CLOCK_APP_URL', 'http://clock_app:5001')

@app.route('/')
def index():
    return render_template('button_index.html')

@app.route('/decrement', methods=['POST'])
def decrement():
    requests.post(f'{CLOCK_APP_URL}/update_time')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
