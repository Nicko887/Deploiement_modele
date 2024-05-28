import requests
import pandas as pd

url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convertir les données JSON en dictionnaire Python
    df = pd.json_normalize(data['data'])  # Convertir le dictionnaire en DataFrame
    # print(df.head(10))  # Afficher les premières lignes du DataFrame
else:
    print("La requête a échoué avec le code d'état :", response.status_code)

# print(df.shape)


import seaborn as sns
from sklearn.linear_model import LogisticRegression
data = sns.load_dataset('iris')
y = data['species']
x = data.drop(columns='species')

model = LogisticRegression().fit(x, y)

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Charger le jeu de données Iris
iris_data = sns.load_dataset('iris')

# Séparer les variables explicatives (features) et la variable cible (target)
x = iris_data.drop(columns='species')
y = iris_data['species']

# Diviser les données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Mise à l'échelle des données
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialiser et entraîner le modèle de régression logistique
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test_scaled)

# Calculer et afficher la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle:", accuracy)

# Afficher le rapport de classification
print("Rapport de classification:")
print(classification_report(y_test, y_pred))

import joblib
model_path = 'C:/Users/nicoe/Desktop/Deploiement model/model.pkl'
joblib.dump(model, model_path)








