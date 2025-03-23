from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)  
    return data

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3169,threaded=True)
