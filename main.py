import sys
import sequencial
import multiprocessos
import threads
import concorrencia
from interface_metodos import executar_interativo, salvar_csv

DOWNLOADS = [100, 500, 1000]
CPUS = [2, 4, 8]

def executar_lote(combinacoes):
    try:
        for func, args in combinacoes:
            print(f"\n{'─'*40}")
            resultado = func(*args)
            if resultado:
                salvar_csv(*resultado)
    except KeyboardInterrupt:
        print("\nLote interrompido pelo usuário.")
        
def combinacoes_sequencial():
    return [(sequencial.sequencial, (d,)) for d in DOWNLOADS]

def combinacoes_metodo(func):
    return [(func, (c, d)) for c in CPUS for d in DOWNLOADS]

def todas_as_30():
    lote = combinacoes_sequencial()
    for func in [multiprocessos.multiprocessos, threads.threads_executor, concorrencia.concorrencia]:
        lote += combinacoes_metodo(func)
    return lote

def submenu_sequencial():
    OPCOES = {
        "1": ("Todas as 3 combinações (100, 500 e 1000 img)", combinacoes_sequencial()),
        "2": ("100 img",                                      [(sequencial.sequencial, (100,))]),
        "3": ("500 img",                                      [(sequencial.sequencial, (500,))]),
        "4": ("1000 img",                                     [(sequencial.sequencial, (1000,))]),
        "5": ("Combinação manual",                            None),
        "0": ("Voltar",                                       None),
    }

    while True:
        print(f"\n{'─'*40}")
        print("  SEQUENCIAL")
        print(f"{'─'*40}")
        for k, (desc, _) in OPCOES.items():
            print(f"  {k}. {desc}")

        opcao = input("\nEscolha: ").strip()

        if opcao == "0":
            break
        elif opcao == "5":
            executar_interativo(sequencial.sequencial)
        elif opcao in OPCOES:
            _, lote = OPCOES[opcao]
            executar_lote(lote)
        else:
            print("Opção inválida.")

def submenu_metodo_paralelo(nome, func):
    OPCOES = {
        "1": ("Todas as 9 combinações",          combinacoes_metodo(func)),
        "2": (f"2 CPUs — 100, 500 e 1000 img",  [(func, (2, d)) for d in DOWNLOADS]),
        "3": (f"4 CPUs — 100, 500 e 1000 img",  [(func, (4, d)) for d in DOWNLOADS]),
        "4": (f"8 CPUs — 100, 500 e 1000 img",  [(func, (8, d)) for d in DOWNLOADS]),
        "5": (f"100 img — 2, 4 e 8 CPUs",       [(func, (c, 100)) for c in CPUS]),
        "6": (f"500 img — 2, 4 e 8 CPUs",       [(func, (c, 500)) for c in CPUS]),
        "7": (f"1000 img — 2, 4 e 8 CPUs",      [(func, (c, 1000)) for c in CPUS]),
        "8": ("Combinação manual",               None),
        "0": ("Voltar",                          None),
    }

    while True:
        print(f"\n{'─'*40}")
        print(f"  {nome.upper()}")
        print(f"{'─'*40}")
        for k, (desc, _) in OPCOES.items():
            print(f"  {k}. {desc}")

        opcao = input("\nEscolha: ").strip()

        if opcao == "0":
            break
        elif opcao == "8":
            executar_interativo(func)
        elif opcao in OPCOES:
            _, lote = OPCOES[opcao]
            executar_lote(lote)
        else:
            print("Opção inválida.")

def main():
    print(f"\n{'═'*40}")
    print("  PROJETO POKÉAPI — MENU PRINCIPAL")
    print(f"{'═'*40}")
    print("  1.  Todas as 30 combinações de uma vez")
    print("  ─")
    print("  2.  Sequencial")
    print("  3.  Multiprocessos")
    print("  4.  Threads")
    print("  5.  Concorrência")
    print("  ─")
    print("  6.  Sair")

    opcao = input("\nEscolha: ").strip()

    if opcao == "1":
        print("\nExecutando todas as 30 combinações...")
        executar_lote(todas_as_30())
    elif opcao == "2":
        submenu_sequencial()
    elif opcao == "3":
        submenu_metodo_paralelo("Multiprocessos", multiprocessos.multiprocessos)
    elif opcao == "4":
        submenu_metodo_paralelo("Threads", threads.threads_executor)
    elif opcao == "5":
        submenu_metodo_paralelo("Concorrência", concorrencia.concorrencia)
    elif opcao == "6":
        sys.exit()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    while True:
        main()
        input("\nPressione Enter para voltar ao menu.")