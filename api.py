from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Bienvenue au nouveau arrivant ! </h1>"

@app.route('/api/v1/residents', methods=['GET'])
def residents():
    residents = [
        {"id": 1, "prenom": "John", "age": 30, "date_arrivee": "2020-01-15"},
        {"id": 2, "prenom": "Jane ", "age": 25, "date_arrivee": "2021-06-10"},
        {"id": 3, "prenom": "Alice", "age": 28, "date_arrivee": "2019-11-20"}
    ]
    return jsonify(residents)

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