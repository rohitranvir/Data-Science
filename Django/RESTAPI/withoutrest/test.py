import requests

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijsoncbv/'

url = requests.delete(BASE_URL + ENDPOINT)

print(url.status_code)
# print(url.text)
print(url.json())