# FastAPI Application

Cette application FastAPI propose trois points de terminaison pour retourner des messages de bienvenue et des nombres aléatoires.

## Prérequis

Avant de lancer l'application, assurez-vous d'avoir les éléments suivants installés :

- Python 3.7 ou supérieur
- `pip`, le gestionnaire de paquets Python

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers dans le répertoire de votre choix.

2. Accédez au répertoire contenant les fichiers de l'application. Par exemple :

    ```bash
    cd C:\Users\nicoe\Desktop\deploiement_model_python
    ```

3. Créez un environnement virtuel (recommandé) et activez-le :

    Sous Windows :
    ```bash
    python -m venv env
    env\Scripts\activate
    ```

    Sous macOS/Linux :
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Installez les dépendances nécessaires :

    ```bash
    pip install fastapi uvicorn
    ```

## Contenu de `main.py`

Voici le code de l'application :

```python
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def acceuil(min: int = 0, max: int = 10):
    return {"message": "Bonjour et bienvenue"}

@app.get("/nombre")
def nombre(min: int = 0, max: int = 10):
    return {"nombre aléatoire entre {} et {}: {}".format(min, max-1, random.randint(min, max))}

@app.get("/nombre2")
def nombre2(min: int = 10, max: int = 100):
    return {"nombre aléatoire entre {} et {}: {}".format(min, max-1, random.randint(min, max))}


Lancement dans le terminal: uvicorn main:app --reload
