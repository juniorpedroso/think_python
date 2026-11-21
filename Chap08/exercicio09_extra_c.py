def head_simples(nome_arquivo, quantidade, arquivo_saida=None):
    """Versão melhorada sem usar islice"""
    linhas_lidas = []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê linha por linha até atingir a quantidade
            for i, linha in enumerate(arquivo):
                if i >= quantidade:
                    break
                linhas_lidas.append(linha)
        
        if arquivo_saida:
            print(f'Gravando {len(linhas_lidas)} linhas...')
            with open(arquivo_saida, 'w', encoding='utf-8') as saida:
                saida.writelines(linhas_lidas)
        else:
            for linha in linhas_lidas:
                print(linha, end='')
                
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
    
    return len(linhas_lidas)
