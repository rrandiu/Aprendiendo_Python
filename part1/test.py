"""import requests

url = 'https://v6.exchangerate-api.com/v6/6c006704ae4031680ffd9318/latest/USD'
response = requests.get(url)
data = response.json()

usd = data['conversion_rates']['PEN']
sueldo = 802.24 * usd
print(sueldo)

from datetime import datetime
print(datetime.today())"""

shift = input("Enter a shift (M, T, or N): ")

while shift not in ['M', 'T', 'N']:
    print("Invalid input. Please enter M, T, or N.")
    shift = input("Enter a shift (M, T, or N): ")

print(f"Valid input: {shift}")