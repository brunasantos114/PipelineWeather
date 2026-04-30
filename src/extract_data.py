# Importações de bibliotecas necessárias
import requests  # Biblioteca para fazer requisições HTTP
import json  # Biblioteca para trabalhar com arquivos JSON
from pathlib import Path  # Biblioteca para manipular caminhos de arquivos
 
 
# Configuração do logging para rastrear eventos e erros
import logging
logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'  
)
 
#api_key = 'aec427025fd9d8b16c56676ddb5ba351'
#url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={api_key}'
 
def extract_weather_data(url: str) -> list:
  
    response = requests.get(url)
    data = response.json()
 
    if response.status_code != 200:
        logging.error("Erro na aquisição")
        return []
    
    if not data:
        logging.warn("Nenhum dado retornado")
        return []
    
    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
 

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
 

    logging.info(f"Arquivo salvo em {output_path}")
    
    return data
 
 
# extract_wheather_data(url)