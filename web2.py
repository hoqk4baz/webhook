from flask import Flask, request, jsonify
from datetime import datetime
import threading
import logging

app = Flask(__name__)

response_data = None

@app.route('/webhook', methods=['POST'])
def webhook():
    global response_data
    data = request.get_json()
    if not data:
        return jsonify({"error": "Geçersiz veri"}), 400 
    
    # Gelen veriyi ve zamanı alıyoruz
    response_data = {
        "time": datetime.now().strftime("%d.%m.%Y=%H:%M"),
        "body": data
    }
    return jsonify(response_data), 200 

@app.route('/sonuc', methods=['GET'])
def get_response():
    if response_data:
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Veri bulunamadı"}), 404

def reset_data():
    global response_data

if __name__ == '__main__':
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['LOGGER_NAME'] = 'flask'
    app.logger.setLevel(logging.ERROR)
    threading.Thread(target=reset_data, daemon=True).start()
    app.run(host='193.111.125.122', port=3132, debug=False)
