import os
import requests
from threading import local

_session_local = local()

def _get_session():
    if not hasattr(_session_local, "session"):
        _session_local.session = requests.Session()
        _session_local.session.headers.update({'User-Agent': 'Mozilla/5.0'})
    return _session_local.session

def baixar_imagem_pokemon(id_pokemon):
    pasta_destino = 'img'
    url_api = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"

    os.makedirs(pasta_destino, exist_ok=True)

    try:
        session = _get_session()

        response = session.get(url_api, timeout=10)
        if response.status_code == 200:
            url_imagem = response.json()['sprites']['front_default']

            if url_imagem:
                img_data = session.get(url_imagem, timeout=10).content
                caminho_completo = os.path.join(pasta_destino, f"{id_pokemon}.png")
                with open(caminho_completo, 'wb') as f:
                    f.write(img_data)
                return True

    except requests.RequestException as e:
        print(f"Erro no download do Pokémon {id_pokemon}: {e}")
    return False