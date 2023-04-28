import requests

url = 'https://v6.exchangerate-api.com/v6/6c006704ae4031680ffd9318/latest/USD'
response = requests.get(url)
data = response.json()

usd = data['conversion_rates']['PEN']
sueldo = 802.24 * usd
print(sueldo)
