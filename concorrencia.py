import time
from concurrent.futures import ThreadPoolExecutor
from download_img import baixar_imagem_pokemon
from apagar_download import limpar_imagens

def concorrencia(n_cpus, quantidade_downloads):
    tempos = []
    metodo = "Concorrência"

    for i in range(1, 11):
        ids = list(range(1, quantidade_downloads + 1))
        
        inicio = time.time()
        
        with ThreadPoolExecutor(max_workers=n_cpus) as executor:
            executor.map(baixar_imagem_pokemon, ids)
            
        fim = time.time()
        tempo_decorrido = fim - inicio
        tempos.append(tempo_decorrido)
        
        print(f"{metodo} | {n_cpus} | {quantidade_downloads} | Tempo individual ({i}): {tempo_decorrido:.2f}s")
        
        limpar_imagens()

    tempo_medio = sum(tempos) / len(tempos)
    print(f"{metodo} | {n_cpus} | {quantidade_downloads} | Tempo médio: {tempo_medio:.2f}s")