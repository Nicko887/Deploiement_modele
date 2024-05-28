import tkinter as tk
from tkinter import messagebox
import requests
import json

# Fonction pour envoyer les données au serveur et recevoir la prédiction
def get_prediction():
    url = "http://127.0.0.1:8000/score"
    data = {
        "sepal_length": sepal_length_var.get(),
        "sepal_width": sepal_width_var.get(),
        "petal_length": petal_length_var.get(),
        "petal_width": petal_width_var.get()
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result_var.set(response.text)
    else:
        messagebox.showerror("Erreur", "La requête a échoué avec le statut : " + str(response.status_code))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Prédiction d'Iris")

# Création des variables tkinter pour stocker les entrées et la prédiction
sepal_length_var = tk.DoubleVar()
sepal_width_var = tk.DoubleVar()
petal_length_var = tk.DoubleVar()
petal_width_var = tk.DoubleVar()
result_var = tk.StringVar()

# Création et placement des widgets pour les entrées
tk.Label(root, text="Longueur du sépale:").grid(row=0, column=0)
tk.Entry(root, textvariable=sepal_length_var).grid(row=0, column=1)

tk.Label(root, text="Largeur du sépale:").grid(row=1, column=0)
tk.Entry(root, textvariable=sepal_width_var).grid(row=1, column=1)

tk.Label(root, text="Longueur du pétale:").grid(row=2, column=0)
tk.Entry(root, textvariable=petal_length_var).grid(row=2, column=1)

tk.Label(root, text="Largeur du pétale:").grid(row=3, column=0)
tk.Entry(root, textvariable=petal_width_var).grid(row=3, column=1)

# Bouton pour envoyer les données et obtenir la prédiction
tk.Button(root, text="Obtenir la prédiction", command=get_prediction).grid(row=4, column=0, columnspan=2)

# Label pour afficher le résultat
tk.Label(root, text="Résultat de prédiction:").grid(row=5, column=0)
tk.Label(root, textvariable=result_var).grid(row=5, column=1)

root.mainloop()
