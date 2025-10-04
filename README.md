# API Mairie - Système de Gestion des Résidents

Une API REST développée avec Flask pour la gestion des résidents d'une commune. Ce projet a été conçue dans le cadre d'un cours d'introduction au système d'information (SI).

## Consignes

Pour accueillir dignement ses nouveaux habitants, le conseil municipal de la ville
a décidé d’offrir un cadeau à tous ses habitants qui soufflent leur première
bougie dans la commune.
- Le rôle de notre application est donc :
- De sélectionner les habitants éligibles à l’obtention d’un cadeau (ils ont emménagé depuis plus
de 1 an)
- Pour chacun des habitants éligibles :
- Trouver le cadeau approprié en fonction de son âge : il y a des cadeaux différents par tranche d’âge
- Envoyer un mail annonçant l’attribution du cadeau
- Envoyer un mail récapitulatif au service cadeau de la mairie avec tous les cadeaux attribués de
la journée.

## Prérequis

- Python 3.7+
- Flask
- Flask-cors
- pip (gestionnaire de packages Python)

## Installation

1. **Clonez le repository**
   ```bash
   git clone https://github.com/EliasKhallouk/APIMairie.git
   cd APIMairie
   ```

2. **Installez les dépendances**
   ```bash
   pip install flask
   pip install flask-cors
   ```

3. **Lancez l'application**
   ```bash
   python api.py
   ```

L'API sera accessible sur `http://localhost:5050`

## Documentation de l'API

### Base URL
```
http://localhost:5050
```


### Page d'accueil
```http
GET /
```
Affiche un message de bienvenue pour les nouveaux arrivants.


### Lister tous les habitants
```http
GET /api/v1/residents
```

**Réponse :**
```json
[
  {
    "id": 1,
    "prenom": "John",
    "age": 30,
    "date_arrivee": "2020-01-15"
  },
  {
    "id": 2,
    "prenom": "Jane",
    "age": 25,
    "date_arrivee": "2021-06-10"
  },
  { "id": 3, 
    "prenom": "Alice", 
    "age": 28, 
    "date_arrivee": "2019-11-20"
  }
]
```

### Détails d'un habitant
```http
GET /api/v1/residents/{id}
```

**Paramètres :**
- `id` (integer) : Identifiant unique du résident

**Réponse :**
```json
{
  "id": 1,
  "prenom": "John",
  "age": 30,
  "date_arrivee": "2020-01-15"
}
```

**Erreurs :**
- `404` : Résident non trouvé

### Ajouter un habitant
```http
POST /api/v1/residents
```

**Corps de la requête :**
```json
{
  "prenom": "Elias",
  "age": 35,
  "date_arrivee": "2023-03-15"
}
```

**Champs obligatoires :**
- `prenom` (string) : Prénom du résident
- `age` (integer) : Âge du résident
- `date_arrivee` (string) : Date d'arrivée au format YYYY-MM-DD

**Réponse :**
```json
{
  "id": 4,
  "prenom": "Elias",
  "age": 35,
  "date_arrivee": "2023-03-15"
}
```

**Erreurs :**
- `400` : Champs requis manquants


### Modifier un résident
```http
PUT /api/v1/residents/{id}
```

**Paramètres :**
- `id` (integer) : Identifiant unique du résident à modifier

**Corps de la requête :**
```json
{
  "prenom": "Nouveau Prénom",
  "age": "Nouvel age",
  "date_arrivee": "Nouvelle date d'arrivée"
}
```

**Champs obligatoires :**
- `prenom` (string) : Nouveau prénom du résident
- `age` (integer) : Nouvel âge du résident
- `date_arrivee` (string) : Nouvelle date d'arrivée au format YYYY-MM-DD

**Réponse :**
```json
{
  "id": 1,
  "prenom": "Nouveau Prénom",
  "age": 28,
  "date_arrivee": "2022-05-10"
}
```

**Erreurs :**
- `404` : Résident non trouvé
- `400` : Champs requis manquants

### Supprimer un résident
```http
DELETE /api/v1/residents/{id}
```

**Paramètres :**
- `id` (integer) : Identifiant unique du résident à supprimer

**Réponse :**
```json
{
  "message": "Résident supprimé avec succès"
}
```

**Erreurs :**
- `404` : Résident non trouvé

### Lister les résidents éligibles aux cadeaux
```http
GET /api/v1/residents/eligible
```

Retourne la liste des résidents éligibles à recevoir un cadeau avec le cadeau approprié selon leur âge.

**Critères d'éligibilité :**
- Le résident doit être présent dans la commune depuis au moins 365 jours

**Attribution des cadeaux par âge :**
- **Moins de 18 ans** : Peluche
- **18-25 ans** : Billet pour un spectacle
- **26-35 ans** : Bon d'achat de 50€
- **Plus de 35 ans** : Panier garni

**Réponse :**
```json
[
  {
    "id": 1,
    "prenom": "John",
    "age": 30,
    "date_arrivee": "2020-01-15",
    "cadeaux": [
      {
        "id": 3,
        "description": "Bon d'achat de 50€"
      }
    ]
  },
  {
    "id": 4,
    "prenom": "Bob",
    "age": 7,
    "date_arrivee": "2019-03-05",
    "cadeaux": [
      {
        "id": 1,
        "description": "Peluche"
      }
    ]
  }
]
```

### Créer des attributions
```http
POST /attributions
```
*Fonctionnalité en cours de développement*



## Contributions

- Elias Khallouk
- Wissam Shaaban
- Alexis Bryon
- David
- Manon
- Christelle Souka
- Yiannis Leblanc

