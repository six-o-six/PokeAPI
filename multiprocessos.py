import time
from multiprocessing import Pool
from download_img import baixar_imagem_pokemon
from apagar_download import limpar_imagens

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
    try:
        cpus = int(input("Quantidade de CPUs (2, 4 ou 8): "))
        downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
        if cpus in [2, 4, 8] and downloads in [100, 500, 1000]:
            multiprocessos(cpus, downloads)
        else:
            print("Valores inválidos para CPU ou Downloads.")
    except ValueError:
        print("Insira números válidos.")