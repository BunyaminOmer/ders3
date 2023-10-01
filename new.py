import requests
status = requests.get("https://www.w3schools.com")
print(status.content)