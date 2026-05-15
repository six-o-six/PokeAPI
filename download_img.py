import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

def baixar_imagem_pokemon(id_pokemon):
    pasta_destino = 'img'
    url_api = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    try:
        request = Request(url_api, headers=headers)
        with urlopen(request, timeout=10) as response:
            if response.status == 200:
                dados = json.load(response)
                url_imagem = dados['sprites']['front_default']
                
                if url_imagem:
                    image_request = Request(url_imagem, headers=headers)
                    with urlopen(image_request, timeout=10) as img_response:
                        img_data = img_response.read()
                    nome_arquivo = f"{id_pokemon}.png"
                    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
                    
                    with open(caminho_completo, 'wb') as f:
                        f.write(img_data)
                    return True
    except (HTTPError, URLError, ValueError) as e:
        print(f"Erro no download do Pokémon {id_pokemon}: {e}")
    return False