import requests


r = requests.get("https://api.github.com")
print("Github Status:" ,r.status_code)