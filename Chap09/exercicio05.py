'''
Exercício 5 – Trabalhando com Strings e listas
Intermediário
Objetivo: praticar split() e join().

Crie uma variável contendo a seguinte frase:
frase = 'Python é uma linguagem de programação'
Seu programa deverá:
1. Transformar a frase em uma lista de palavras.
2. Imprimir a lista.
3. Mostrar quantas palavras existem.
4. Ordenar as palavras alfabeticamente.
5. Juntar novamente as palavras utilizando join().
6. Imprimir a nova frase.
'''

frase = 'Python é uma linguagem de programação'

# transformar a frase em uma lista de palavras
palavras = frase.split()
# imprimir a lista
print(palavras)
# mostrar quantas palavras existem
print(f'Quantidade de palavras: {len(palavras)}')
# ordenar as palavras alfabeticamente
palavras_alf = sorted(palavras)
# juntar as palavras usando join()
nova_frase = ' '.join(palavras_alf)
# imprimir a nova frase
print(nova_frase)
