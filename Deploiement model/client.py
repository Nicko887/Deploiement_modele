import requests
import json
import pandas as pd

url = "http://127.0.0.1:8000/score"
data = json.dumps({"quelque chose": "en entrée"})

data_sent = json.dumps({"sepal_length": 6.7,
        "sepal_width": 3,
        "petal_length": 5.2,
        "petal_width": 2.3
    })

response = requests.request('POST', url=url, data=data_sent)

response.text
response.status_code
print(response.text)
