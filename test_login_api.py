```python
import os
import requests

URL = "https://devapi.mesign.id/api/auth/user"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/json",
}

payload = {
    "username": os.getenv("API_USERNAME"),
    "password": os.getenv("API_PASSWORD"),
    "longitude": "-1120.084",
    "latitude": "370.4219983",
    "token": {
        "deviceId": "TesDevice",
        "token": "00859221"
    },
    "mobile": True,
    "ip": "192.168.0.1",
    "country": "",
    "cf-turnstile-response": os.getenv("CF_TURNSTILE_RESPONSE"),
}

response = requests.post(
    URL,
    headers=headers,
    json=payload,
    timeout=30
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)

# Basic API assertion
assert response.status_code == 200, (
    f"API failed. Expected 200, got {response.status_code}"
)

print("API TEST PASSED")
```
