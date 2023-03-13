from django.shortcuts import render
from pathlib import Path, os
from dotenv import load_dotenv
import requests
import json

from setup.settings import BASE_DIR


def index(request):
    load_dotenv()

    #API_KEY = str(os.getenv('API_KEY'))
    API_KEY = '38e6287279387e1e84fe95a9cb42a9bf'
    cidade = 'florianópolis'
    '''
    link_tempo_atual = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao_tempo_atual = requests.get(link_tempo_atual)
    requisicao_tempo_atual_dic = requisicao_tempo_atual.json()
    
    nome_cidade = requisicao_tempo_atual_dic['name']
    lat = requisicao_tempo_atual_dic['coord']['lat']
    lon = requisicao_tempo_atual_dic['coord']['lon']

    link_previsao_5_dias = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    requisicao_previsao_5_dias = requests.get(link_previsao_5_dias)
    requisicao_previsao_5_dias_dic = requisicao_previsao_5_dias.json()


    # Salvando os arquivos json retornado pelas requisições...
    json_object = json.dumps(requisicao_tempo_atual_dic, indent = 4) 
    with open(os.path.join(BASE_DIR, 'req_json/tempo_atual.json'), "w") as outfile: 
        outfile.write(json_object) 

    json_object = json.dumps(requisicao_previsao_5_dias_dic, indent = 4) 
    with open(os.path.join(BASE_DIR, 'req_json/previsao_5_dias.json'), "w") as outfile: 
        outfile.write(json_object) '''

    
    #print(requisicao_tempo_atual_dic)
    #print('###################################')
    #print(requisicao_previsao_5_dias_dic)

    #descricao = requisicao_dic['weather'][0]['description']
    #temperatura = requisicao_dic['main']['temp']-273.15

    #print(descricao, f"{temperatura}°C")

    #print(requisicao_dic['coord']['lon'])

    return(render(request, 'previsao_do_tempo/index.html'))