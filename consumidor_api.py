import requests 

def obter_dados():

    url = "http://127.0.0.1:8000/v1/forecast"

    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados["current"]["temperature_2m"]
        umidade = dados["current"]["relative_humidity_2m"]
        sensacao = dados["current"]["apparent_temperature"]
        precipitacao = dados["current"]["precipitation"]
        vento = dados["current"]["wind_speed_10m"]
        data = dados["current"]["time"]

        print(f"A temperatura é: {temperatura}")
        print(f"A umidade é: {umidade}")
        print(f"A sensação térmica é: {sensacao}")
        print(f"A precipitação de chuva é: {precipitacao}")
        print(f"A velocidade do vento é: {vento}")
        print(f"Data/hora: {data}")
        return dados
    
    else:
        print("Tente novamente.")

obter_dados()