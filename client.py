
import requests

BASE_URL = "http://localhost:8000"

# Health check
resp = requests.get(BASE_URL + "/")
print("Health:", resp.json())

# Create item
item = {"name": "apple", "price": 12.5}
resp = requests.post(BASE_URL + "/items", json=item)
print("Created:", resp.json())
