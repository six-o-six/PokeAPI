import sys
import sequencial
import multiprocessos
import threads
import concorrencia
from interface_metodos import executar_interativo

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
        executar_interativo(sequencial.sequencial)
    elif opcao == '2':
        executar_interativo(multiprocessos.multiprocessos)
    elif opcao == '3':
        executar_interativo(threads.threads_executor)
    elif opcao == '4':
        executar_interativo(concorrencia.concorrencia)
    elif opcao == '5':
        sys.exit()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main() 