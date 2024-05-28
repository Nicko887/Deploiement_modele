import os

def create_directory_structure(root_dir):
    # Définition de la structure de répertoires
    directories = {
        'data': ['brute', 'preparee'],
        'code': [],
        'documentation': [],
        'models': [],
        'notebooks': [],
        'rapport': []
    }

    # Création des répertoires
    for directory, subdirs in directories.items():
        directory_path = os.path.join(root_dir, directory)
        os.makedirs(directory_path, exist_ok=True)
        for subdir in subdirs:
            subdir_path = os.path.join(directory_path, subdir)
            os.makedirs(subdir_path, exist_ok=True)

    # Création des fichiers vides
    empty_files = {
        'data/brute/jeu_de_donnees_brut.csv': '',
        'data/preparee/jeu_de_donnees_preparee.csv': '',
        'code/apprentissage.py': '',
        'code/evaluation.py': '',
        'code/preparee_donnees.py': '',
        'code/visualisation.py': '',
        'documentation/README.md': '',
        'models/modele_acp.pkl': '',  # Fichiers de modèle vides
        'models/modele_classification.pkl': '',  # Fichiers de modèle vides
        'notebooks/exploration_donnees.ipynb': '',
        'notebooks/selection_modele.ipynb': '',
        'rapport/rapport_analyse.pdf': '',
        'requirements.txt': ''
    }

    # Création des fichiers
    for file, content in empty_files.items():
        file_path = os.path.join(root_dir, file)
        with open(file_path, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    root_directory = r'C:\Users\nicoe\Desktop\Utiliser_Terminal\projet_data_science'
    create_directory_structure(root_directory)
    print("Structure de répertoires créée avec succès.")
