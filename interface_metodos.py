import inspect
import csv
import os
from datetime import datetime

def salvar_csv(metodo, n_cpus, quantidade_downloads, tempos, tempo_medio):
    arquivo = "resultados.csv"
    cabecalho = ["timestamp", "metodo", "cpus", "downloads", "iteracao", "tempo_s", "tempo_medio_s"]
    novo = not os.path.exists(arquivo)

    with open(arquivo, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cabecalho)
        if novo:
            writer.writeheader()
        ts = datetime.now().isoformat()
        for i, t in enumerate(tempos, start=1):
            writer.writerow({
                "timestamp": ts,
                "metodo": metodo,
                "cpus": n_cpus,
                "downloads": quantidade_downloads,
                "iteracao": i,
                "tempo_s": round(t, 2),
                "tempo_medio_s": round(tempo_medio, 2)
            })

def executar_interativo(func_execucao, loop_continuo=False):
    while True:
        try:
            sig = inspect.signature(func_execucao)
            params = sig.parameters

            if len(params) == 1:
                downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
                if downloads in [100, 500, 1000]:
                    resultado = func_execucao(downloads)
                    if resultado:
                        salvar_csv(*resultado)
                else:
                    print("Valor inválido para Downloads.")

            elif len(params) == 2:
                cpus = int(input("Quantidade de CPUs (2, 4 ou 8): "))
                downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
                if cpus in [2, 4, 8] and downloads in [100, 500, 1000]:
                    resultado = func_execucao(cpus, downloads)
                    if resultado:
                        salvar_csv(*resultado)
                else:
                    print("Valores inválidos para CPU ou Downloads.")

            if not loop_continuo:
                break
            else:
                print("\n" + "-"*40)
                input("Pressione Enter para rodar novamente ou Ctrl+C para sair.")
                print("-"*40 + "\n")

        except ValueError:
            print("Erro: Insira apenas números inteiros.")
        except KeyboardInterrupt:
            print("\nExecução interrompida pelo usuário. Saindo...")
            break