import seaborn as sn
data = sn.load_dataset('iris')

# print(data.head())
des = data.describe(include=['object'])
print(des)

import pandas as pd

# Supposons que vous ayez déjà chargé votre jeu de données dans une DataFrame appelée 'data'

# Sélectionner les colonnes catégorielles
categorical_columns = data.select_dtypes(include=['object'])
print("{categorical_columns} bonjour")

# Parcourir chaque colonne catégorielle et compter les occurrences de chaque valeur unique
for column in categorical_columns:
    print(f"Nombre d'occurrences pour la colonne '{column}':")
    print(data[column].value_counts())
    print()  


# Sélectionner les colonnes quantitatives
numeric_columns = data.select_dtypes(include=['int', 'float'])

# Afficher les statistiques descriptives pour les colonnes quantitatives
print("Statistiques descriptives pour les variables quantitatives :")
print(data.describe())

