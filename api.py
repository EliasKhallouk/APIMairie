from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/hello/<name>', methods=['GET'])
def hello():
    return "<h1>Bienvenue au nouveau arrivant ! </h1>"

if __name__ == '__main__':
    app.run(port=5050, use_reloader=True)