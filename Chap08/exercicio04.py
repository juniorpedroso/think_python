'''
Um palíndromo é uma palavra que pode ser lida da esquerda para a direita ou da direita para a esquerda.

Exemplos:
- arara
- radar
- ovo
- osso

Crie uma função. 
Ela deverá retornar:
- True se a palavra for um palíndromo.
- False caso contrário.
Desafio: faça com que a função ignore espaços e diferenças entre maiúsculas e minúsculas.
'''

import re

def is_palindrome(palavra):
    # Seu código aqui
    palavra_min = palavra.lower()
    palavra_limpa = palavra_min.strip()
    comprimento = len(palavra_limpa)
    metade = comprimento // 2
    palavra_par = comprimento % 2 == 0

    # retira o final da palavra
    if palavra_par:
        palavra_fin = palavra_limpa[metade:]
    else:
        palavra_fin = palavra_limpa[(metade + 1):]

    # retira a primeira metade da palavra e inverte a letras
    palavra_ini = ''
    for letra in range(metade, 0, -1):
        palavra_ini += palavra_limpa[letra - 1]

    # verifica se o final da palavra é igual ao começo invertido
    if palavra_fin == palavra_ini:
        return True
    else:
        return False


is_palindrome('   arara')
