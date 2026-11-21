'''
O livro propõe um exercício interessante: implementar uma função semelhante ao comando head do Linux.
O comando head mostra as primeiras linhas de um arquivo.
Sua missão:
Criar uma função:
def head(nome_arquivo, quantidade, arquivo_saida=None):
    pass
    
Ela deverá:
- Receber o nome de um arquivo.
- Receber a quantidade de linhas que deseja ler.
- Se arquivo_saida for None, mostrar as linhas na tela.
- Caso contrário, gravar as linhas em outro arquivo.
Esse exercício é excelente para praticar manipulação de arquivos e funções.
'''

def head(nome_arquivo, quantidade, arquivo_saida=None):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    # se houver o nome de um arquivo de saída
    if arquivo_saida:
        with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            for i, linha in enumerate(conteudo.splitlines()):
                if i >= quantidade:
                    break
                arquivo_saida.write(linha + '\n')

        print('Gravando.....')

    # se não houver um arquivo de saída
    else:
        for i, linha in enumerate(conteudo.splitlines()):
            if i >= quantidade:
                break
            print(linha)

# head('mensagem.txt', 2)
head('mensagem.txt', 1, 'mensagem_nova.txt')