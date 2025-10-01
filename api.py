from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/hello/<name>', methods=['GET'])
def hello():
    return "<h1>Bienvenue au nouveau arrivant ! </h1>"

@app.route('/residents', methods=['GET'])
def residents():
    pass

@app.route('/residents/<id>', methods=['GET'])
def get_resident(id: str):
    pass

@app.route('/residents', methods=['POST'])
def add_resident():
    pass

@app.route('/residents/<id>', methods=['PUT'])
def update_resident(id: str):
    pass

@app.route('/residents/<id>', methods=['DELETE'])
def delete_resident(id: str):
    pass

@app.route('/eligible', methods=['GET'])
def get_eligibles():
    pass

@app.route('/attributions', methods=['POST'])
def create_attributions():
    pass

if __name__ == '__main__':
    app.run(port=5050, use_reloader=True)