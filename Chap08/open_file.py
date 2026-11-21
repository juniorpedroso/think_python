# Criando arquivo
arquivo = open('mensagem.txt', 'w', encoding='utf-8')
arquivo.write('Estou estudando Python!\n')
arquivo.write('Estou aprendendo strings.\n')

arquivo.close()

# Lendo arquivo
arquivo = open('mensagem.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)

arquivo.close()

arquivo = open('mensagem.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print(linha.strip())

arquivo.close()
