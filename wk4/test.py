
import requests

payload = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=payload)

print(response.json())