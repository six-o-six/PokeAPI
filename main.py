import sys
from sequencial import sequencial
from multiprocessos import multiprocessos
from threads import threads_executor
from concorrencia import concorrencia

def main():
    print("-" * 30)
    print("PROJETO POKÉAPI - MENU PRINCIPAL")
    print("-" * 30)
    print("1. Executar Sequencial")
    print("2. Executar Multiprocessos")
    print("3. Executar Threads")
    print("4. Executar Concorrência")
    print("5. Sair")

    opcao = input("\nEscolha o método: ")

    if opcao == '1':
        try:
            downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
            if downloads in [100, 500, 1000]:
                sequencial(downloads)
            else:
                    print("Valor inválido para Downloads.")
        except ValueError:
            print("Insira um número válido.")
    
    elif opcao == '2':
        try:
            cpus = int(input("Quantidade de CPUs (2, 4 ou 8): "))
            downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
            if cpus in [2, 4, 8] and downloads in [100, 500, 1000]:
                multiprocessos(cpus, downloads)
            else:
                print("Valores inválidos para CPU ou Downloads.")
        except ValueError:
            print("Insira números válidos.")
            
    elif opcao == '3':
        try:
            cpus = int(input("Quantidade de CPUs (2, 4 ou 8): "))
            downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
            if cpus in [2, 4, 8] and downloads in [100, 500, 1000]:
                threads_executor(cpus, downloads)
            else:
                print("Valores inválidos para CPU ou Downloads.")
        except ValueError:
            print("Insira números válidos.")
            
    elif opcao == '4':
        try:
            cpus = int(input("Quantidade de CPUs (2, 4 ou 8): "))
            downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
            if cpus in [2, 4, 8] and downloads in [100, 500, 1000]:
                concorrencia(cpus, downloads)
            else:
                print("Valores inválidos para CPU ou Downloads.")
        except ValueError:
            print("Insira números válidos.")
    
    elif opcao == '5':
        sys.exit()
    
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main() 