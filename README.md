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


# Ajouter le service en production

Copier le fichier exploit/edp-documents.service dans /etc/systemd/system et vérifier les élements et modifier le port si nécessaire

Rechargez systemd : 
    
    sudo systemctl daemon-reload

Activez le service :

     sudo systemctl enable edp-documents

Démarrer le service : 
    
    sudo systemctl enable edp-documents


Le serveur se lance sur http://127.0.0.1:8000
Le swagger est accessible sur http://127.0.0.1:8000/docs

# Config

Dans le fichier config.py il est possible de modifier plusieurs paramètres :
- BASE_DIR : chemin vers le dossier courant de l'app (à éviter de modifier car les autres chemin en dépendent)
- UPLOAD_DIR : dossier de destination des fichiers téléversés