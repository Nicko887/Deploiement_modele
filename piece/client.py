import requests
import json

url = "http://127.0.0.1:8000/predict"
data = {
    "sepal_length": 5.5,
    "sepal_width": 4.2,
    "petal_length": 1.4,
    "petal_width": 0.2
}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
