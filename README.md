# py-documents-api
Light API to manage documents

# Installation

- Création de l'environnement virtuel :
Se mettre dans le dossier voulu puis 

    $ python3 -m venv env

- Activation de l'environnement :

    source env/bin/activate

Ce qu'on doit voir une fois activé => (env) loic@portable-4:

"deactivate" pour couper l'environnement. 

- Installation de FastAPI 
Mettre à jour pip avec 

    python -m pip install --upgrade pip

Installer les dépendances nécessaires (dont FastAPI) 

    $ pip install -r /chemin/vers/requirements.txt (le fichier est présent dans le projet)

# Démarrage 

Lancement en mode dev avec rechargement à chaque modification (à n'utiliser que pour tester car lourd en utilisation)

    fastapi dev main.py ou uvicorn main:app --reload

Lancement en mode production

    uvicorn main:app --host 127.0.0.1 --port 8000

Le serveur se lance sur http://127.0.0.1:8000
Le swagger est accessible sur http://127.0.0.1:8000/docs