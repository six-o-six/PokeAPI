import time
from download_img import baixar_imagem_pokemon
from apagar_download import limpar_imagens

def sequencial(quantidade_downloads):
    tempos = []
    metodo = "Sequencial"
    cpus = 1

    for i in range(1, 11):
        inicio = time.time()
        for pokemon_id in range(1, quantidade_downloads + 1):
            baixar_imagem_pokemon(pokemon_id)
            
        fim = time.time()
        tempo_decorrido = fim - inicio
        tempos.append(tempo_decorrido)
        
        print(f"{metodo} | {cpus} | {quantidade_downloads} | Tempo individual ({i}): {tempo_decorrido:.2f}s")
        limpar_imagens()

    tempo_medio = sum(tempos) / len(tempos)
    print(f"{metodo} | {cpus} | {quantidade_downloads} | Tempo médio: {tempo_medio:.2f}s")
    
if __name__ == "__main__":
    try:
        downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
        if downloads in [100, 500, 1000]:
            sequencial(downloads)
        else:
                print("Valor inválido para Downloads.")
    except ValueError:
        print("Insira um número válido.")