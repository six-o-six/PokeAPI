import inspect 

def executar_interativo(func_execucao, loop_continuo=False):
    while True:
        try:
            sig = inspect.signature(func_execucao)
            params = sig.parameters
            
            if len(params) == 1:
                downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
                if downloads in [100, 500, 1000]:
                    func_execucao(downloads)
                else:
                    print("Valor inválido para Downloads.")
            
            elif len(params) == 2:
                cpus = int(input("Quantidade de CPUs (2, 4 ou 8): "))
                downloads = int(input("Quantidade de downloads (100, 500 ou 1000): "))
                
                if cpus in [2, 4, 8] and downloads in [100, 500, 1000]:
                    func_execucao(cpus, downloads)
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
            print("\n\nExecução interrompida pelo usuário. Saindo...")
            break