from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

time_offset = 0

@app.route('/')
def index():
    current_time = datetime.datetime.now() - datetime.timedelta(seconds=time_offset)
    return render_template('clock_index.html', current_time=current_time.strftime('%H:%M:%S'))

@app.route('/update_time', methods=['POST'])
def update_time():
    global time_offset
    time_offset += 10
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
