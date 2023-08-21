import requests
import json


res = requests.get('https://hp-api.onrender.com/api/spells')

if res.status_code == 200:
    dados = json.loads(res.text)
else:
    print(f'Erro: {res.status_code}')
    dados = None