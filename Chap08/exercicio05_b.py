'''
Exercício 5 - Trabalhando com Arquivos
Crie um programa que:
1. Solicite ao usuário três frases.
2. Grave essas frases em um arquivo chamado mensagem.txt.
3. Abra o arquivo novamente.
4. Leia seu conteúdo.
5. Conte quantas linhas existem.
6. Conte quantas vezes aparece a palavra Python.
Utilize open(), write(), read() e close().
'''
# 1. Solicite ao usuário três frases.
frase1 = input('Digite a primeira frase: ')
frase2 = input('Digite a segunda frase: ')
frase3 = input('Digite a terceira frase: ')

# 2. Grave essas frases em um arquivo chamado mensagem.txt.
with open('mensagem05.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(frase1 + '\n')
    arquivo.write(frase2 + '\n')
    arquivo.write(frase3 + '\n')

# 3. Abra o arquivo novamente.
# 4. Leia seu conteúdo.
with open('mensagem05.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

# 5. Conte quantas linhas existem.
qtd_linhas = conteudo.count('\n')

# 6. Conte quantas vezes aparece a palavra Python.
qtd_Python = conteudo.count('Python')


print(f'Qtd de linhas: {qtd_linhas}')
print(f'Qtd de Python: {qtd_Python}')
