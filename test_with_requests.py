import requests

url = "http://127.0.0.1:8034/predict"

input_data = {
    "size": 100,        # house size in square meters
    "bedrooms": 3,      # number of bedrooms
    "garden": 1         # 1 for having a garden, 0 for no garden
}

response = requests.post(url, json=input_data)
print(response.json())

