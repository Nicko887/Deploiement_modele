import os

# Chemin du répertoire du projet
chemin_projet = r'C:\Users\nicoe\Desktop\Utiliser_Terminal\projet_analyse_donnees'

# Liste des répertoires à créer
repertoires = [
    'data/brute',
    'data/preparee',
    'code',
    'documentation',
    'notebooks',
    'rapport'
]

# Liste des fichiers à créer avec leur contenu
fichiers = {
    'data/brute/fichier_donnees_brutes.csv': 'Bonjour',
    'data/preparee/fichier_donnees_preparee.csv': '',
    'code/analyse.py': '',
    'code/visualisation.py': '',
    'documentation/README.md': '',
    'notebooks/exploration_donnees.ipynb': '',
    'rapport/rapport_analyse.pdf': '',
    'requirements.txt': ''
}

# Création des répertoires
for repertoire in repertoires:
    chemin_repertoire = os.path.join(chemin_projet, repertoire)
    os.makedirs(chemin_repertoire, exist_ok=True)

# Création des fichiers avec leur contenu
for fichier, contenu in fichiers.items():
    chemin_fichier = os.path.join(chemin_projet, fichier)
    with open(chemin_fichier, 'w') as f:
        f.write(contenu)

print("Arborescence et fichiers créés avec succès.")
