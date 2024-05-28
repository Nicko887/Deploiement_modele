import joblib
model_import = joblib.load('C:/Users/nicoe/Desktop/Deploiement model/model.pkl')

import joblib
from sklearn.metrics import accuracy_score, classification_report

# Charger le modèle importé
model_import = joblib.load('C:/Users/nicoe/Desktop/Deploiement model/model.pkl')

# Charger les données de test
X_test = ...  # Charger vos données de test
y_test = ...  # Charger vos étiquettes de test

# Faire des prédictions sur l'ensemble de test
y_pred = model_import.predict(X_test)

# Calculer la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle:", accuracy)

# Afficher le rapport de classification
print("Rapport de classification:")
print(classification_report(y_test, y_pred))
