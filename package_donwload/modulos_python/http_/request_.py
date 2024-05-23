# requests para requisições HTTP
# pip install requests types-requests
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> porta 80
# https:// -> porta 443

url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
print(response.text)
