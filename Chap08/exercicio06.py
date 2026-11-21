'''
Exercício 6 – Expressões Regulares
Utilizando o módulo re, crie um programa que analise o texto abaixo:

Seu programa deverá:
1. Localizar todos os números.
2. Mostrar cada número encontrado.
3. Contar quantos números existem.
4. Mostrar a soma das idades.
Dica: pesquise como utilizar re.findall().

'''
texto = '''
João tem 25 anos.
Maria tem 32 anos.
Pedro tem 18 anos.
Ana tem 45 anos.
'''

import re

# padrão de busca
padrao = r'\d+'

# 1 Localizar todos os números com findall
numeros = re.findall(padrao, texto)

# 2 Mostrar cada numero encontrado e calcula o total de idade


# 3 Contar quantos números existem
cont_numeros = 0
total_idade = 0
for r in numeros:
    print(r)
    cont_numeros += 1
    total_idade += int(r)
print(f'Qtd de números: {cont_numeros}')

# 4 Mostrar a soma das idades
print(f'Total de idade = {total_idade}')
