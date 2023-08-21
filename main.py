# https://hp-api.onrender.com/

import requests
import json
import pandas as pd
from translate import Translator

res = requests.get('https://hp-api.onrender.com/api/spells')

if res.status_code == 200:
    dados = json.loads(res.text)
else:
    print(f'Erro: {res.status_code}')
    dados = None

translator = Translator(to_lang="pt")

dados_traduzidos = []

for dado in dados:
    descricao = translator.translate(dado['description'])
    dados_traduzidos.append(
        [
            dado['id'],
            dado['name'],
            descricao
        ]
    )
    print(f'{len(dados_traduzidos)}/{len(dados)}')

colunas = ['id', 'nome', 'descrição']

resultado = pd.DataFrame(dados_traduzidos, columns=colunas)

resultado.to_csv('hp_feiticos.csv')