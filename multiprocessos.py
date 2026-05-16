import time
from multiprocessing import Pool
from download_img import baixar_imagem_pokemon
from apagar_download import limpar_imagens
from interface_metodos import executar_interativo

def multiprocessos(n_cpus, quantidade_downloads):
    tempos = []
    metodo = "Multiprocessos"

    for i in range(1, 11):
        ids = list(range(1, quantidade_downloads + 1))
        
        inicio = time.time()
        with Pool(processes=n_cpus) as pool:
            pool.map(baixar_imagem_pokemon, ids)
            
        fim = time.time()
        tempo_decorrido = fim - inicio
        tempos.append(tempo_decorrido)
        
        print(f"{metodo} | {n_cpus} | {quantidade_downloads} | Tempo individual ({i}): {tempo_decorrido:.2f}s")
        limpar_imagens()

    tempo_medio = sum(tempos) / len(tempos)
    print(f"{metodo} | {n_cpus} | {quantidade_downloads} | Tempo médio: {tempo_medio:.2f}s")
    
if __name__ == "__main__":
    executar_interativo(multiprocessos, loop_continuo=True)