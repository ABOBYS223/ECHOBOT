


import requests

BASE_URL = 'https://api.telegram.org/bot'

from config import TOKEN

def get_updates():
   r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates?offset=1&timeout=10')
   print(r.json())


get_updates()