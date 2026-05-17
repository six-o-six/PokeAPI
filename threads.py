import time
import threading
from download_img import baixar_imagem_pokemon
from apagar_download import limpar_imagens
from interface_metodos import executar_interativo

def threads_executor(n_cpus, quantidade_downloads):
    tempos = []
    metodo = "Threads"

    for i in range(1, 11):
        ids = list(range(1, quantidade_downloads + 1))
        
        inicio = time.time()
        
        for bloco in range(0, len(ids), n_cpus):
            lote_atual = ids[bloco:bloco + n_cpus]
            threads = []
            
            for id_pokemon in lote_atual:
                t = threading.Thread(target=baixar_imagem_pokemon, args=(id_pokemon,))
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()
            
        fim = time.time()
        tempo_decorrido = fim - inicio
        tempos.append(tempo_decorrido)
        
        print(f"{metodo} | {n_cpus} | {quantidade_downloads} | Tempo individual ({i}): {tempo_decorrido:.2f}s")
        limpar_imagens()

    tempo_medio = sum(tempos) / len(tempos)
    print(f"{metodo} | {n_cpus} | {quantidade_downloads} | Tempo médio: {tempo_medio:.2f}s")
    
if __name__ == "__main__":
    executar_interativo(threads_executor, loop_continuo=True)