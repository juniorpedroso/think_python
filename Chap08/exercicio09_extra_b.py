from itertools import islice

def head(nome_arquivo, quantidade, arquivo_saida=None):
    """
    Lê as primeiras N linhas de um arquivo.
    
    Args:
        nome_arquivo (str): Caminho do arquivo de entrada
        quantidade (int): Número de linhas a ler
        arquivo_saida (str, optional): Caminho do arquivo de saída. 
                                        Se None, imprime na tela.
    
    Returns:
        int: Número de linhas processadas
    """
    linhas_processadas = 0
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # islice pega apenas as N primeiras linhas (eficiente!)
            linhas = list(islice(arquivo, quantidade))
            
            if arquivo_saida:
                print(f'Gravando {len(linhas)} linhas em {arquivo_saida}...')
                with open(arquivo_saida, 'w', encoding='utf-8') as saida:
                    saida.writelines(linhas)
            else:
                for linha in linhas:
                    print(linha, end='')  # end='' evita linha extra
            
            linhas_processadas = len(linhas)
            
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    
    return linhas_processadas


# Testes
print("=== Teste 1: Imprimir na tela ===")
head('mensagem.txt', 3)

print("\n=== Teste 2: Gravar em arquivo ===")
head('mensagem.txt', 5, 'mensagem_nova.txt')