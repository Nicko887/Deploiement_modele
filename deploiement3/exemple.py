import json

# Charger le fichier JSON contenant les rapports d'erreurs
with open('errors.json', 'r') as f:
    error_reports = json.load(f)

# Exemple d'utilisation
code_401_message = error_reports["502"]["message"]
print(code_401_message)  
