import requests

# Local Flask server
url = "http://127.0.0.1:5000/predict"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

# To Run the docker version
# url = "http://127.0.0.1:9696/predict"
# client = {"job": "retired", "duration": 445, "poutcome": "success"}

print(requests.post(url, json=client).json())