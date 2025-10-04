from flask import Flask, abort, jsonify, request
from datetime import datetime
from flask_cors import CORS
    
app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


residents = [
    {"id": 1, "prenom": "John", "age": 30, "date_arrivee": "2020-01-15"},
    {"id": 2, "prenom": "Jane ", "age": 25, "date_arrivee": "2021-06-10"},
    {"id": 3, "prenom": "Alice", "age": 28, "date_arrivee": "2025-11-20"},
    {"id": 4, "prenom": "Bob", "age": 7, "date_arrivee": "2019-03-05"},
    {"id": 5, "prenom": "Charlie", "age": 40, "date_arrivee": "2018-07-22"},
    {"id": 6, "prenom": "Diana", "age": 32, "date_arrivee": "2022-02-14"}
]

cadeaux = [
    {"id": 1, "description": "Peluche"},
    {"id": 2, "description": "Billet pour un spectacle"},
    {"id": 3, "description": "Bon d'achat de 50€"},
    {"id": 4, "description": "Panier garni"}
]

# PAGE D'ACCUEIL
@app.route('/', methods=['GET'])
def home():
    return "<h1>Bienvenue au nouveau arrivant ! </h1>"

# LISTE DES HABITANT
@app.route('/api/v1/residents', methods=['GET'])
def get_residents():
    return jsonify(residents), 200

# DÉTAIL D'UN HABITANT
@app.route('/api/v1/residents/<int:resident_id>', methods=['GET'])
def get_resident(resident_id):
    resident = next((r for r in residents if r["id"] == resident_id), None)
    if resident is None:
        abort(404, description=f"Résident avec id {resident_id} non trouvé")
    return jsonify(resident), 200

# AJOUTER UN HABITANT
@app.route('/api/v1/residents', methods=['POST'])
def add_resident():
    data = request.get_json()
    required_fields = {"prenom", "age", "date_arrivee"}
    if not required_fields.issubset(data):
        abort(400, description="Champs requis manquants")
    new_id = max(r["id"] for r in residents) + 1 if residents else 1
    new_resident = {
        "id": new_id,
        "prenom": data["prenom"],
        "age": data["age"],
        "date_arrivee": data["date_arrivee"]
    }
    residents.append(new_resident)
    return jsonify(new_resident), 200
    
# MODIFIER UN HABITANT
@app.route('/api/v1/residents/<int:resident_id>', methods=['PUT'])
def update_resident(resident_id):
    resident = next((r for r in residents if r["id"] == resident_id), None)
    if resident is None:
        abort(404, description=f"Résident avec id {resident_id} non trouvé")

    data = request.get_json()
    required_fields = {"prenom", "age", "date_arrivee"}
    if not required_fields.issubset(data):
        abort(400, description="Champs requis manquants")

    resident["prenom"] = data["prenom"]
    resident["age"] = data["age"]
    resident["date_arrivee"] = data["date_arrivee"]
    return jsonify(resident), 200

# SUPPRIMER UN HABITANT
@app.route('/api/v1/residents/<int:resident_id>', methods=['DELETE'])
def delete_resident(resident_id):
    resident = next((r for r in residents if r["id"] == resident_id), None)
    if resident is None:
        abort(404, description=f"Résident avec id {resident_id} non trouvé")
    residents.remove(resident)
    return jsonify({"message": "Résident supprimé avec succès"}), 200

# LISTE DES HABITANTS ÉLIGIBLES + CADEAU ASSOCIÉ
@app.route('/api/v1/residents/eligible', methods=['GET'])
def get_eligibles():
    today = datetime.today()
    eligible_residents = []
    for r in residents:
        date_arrivee = datetime.strptime(r["date_arrivee"], "%Y-%m-%d")
        if (today - date_arrivee).days >= 365:
            
            if r["age"] < 18:
                cadeaux_ass = [cadeaux[0]]  # Peluche
            elif r["age"] >= 18 and r["age"] <= 25:
                cadeaux_ass = [cadeaux[1]]  # Billet pour un spectacle
            elif r["age"] >= 26 and r["age"] <= 35:
                cadeaux_ass = [cadeaux[2]]  # Bon d'achat de 50€
            else:
                cadeaux_ass = [cadeaux[3]]  # Panier garni

            r["cadeaux"] = cadeaux_ass
            eligible_residents.append(r)
    return jsonify(eligible_residents), 200

@app.route('/attributions', methods=['POST'])
def create_attributions():
    pass

if __name__ == '__main__':
    app.run(port=5050, use_reloader=True)