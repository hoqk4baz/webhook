from flask import Flask, request, jsonify
from datetime import datetime
import threading
import time
import logging

app = Flask(__name__)

response_data = None

@app.route('/webhook', methods=['POST'])
def webhook():
    global response_data
    data = request.get_data(as_text=True)
    response_data = {
        "time": datetime.now().strftime("%d.%m.%Y=%H:%M"),
        "body": data
    }
    return response_data

@app.route('/sonuc', methods=['GET'])
def get_response():
    if response_data:
        return jsonify(response_data)
    else:
        return jsonify({"error": "veri bulunamadi"}), 404


def reset_data():
    global response_data
    while True:
        time.sleep(300)
        response_data = None


if __name__ == '__main__':
    logging.getLogger('werkzeug').setLevel(logging.ERROR) 
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['LOGGER_NAME'] = 'flask'
    app.logger.setLevel(logging.ERROR)
    threading.Thread(target=reset_data, daemon=True).start()
    app.run(host='193.111.125.122', port=3131,debug=False)
