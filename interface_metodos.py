import inspect 

def executar_interativo(func_execucao):
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
                
    except ValueError:
        print("Erro: Insira apenas números inteiros.")