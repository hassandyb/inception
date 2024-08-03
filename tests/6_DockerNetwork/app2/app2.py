from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.form['message']
    print(f"Received message: {data}")
    return "Message received!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
