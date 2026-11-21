import re

'''
Exercício 8 – Desafio Final: Analisador de Texto
Desafio intermediário
Crie um programa que receba um texto digitado pelo usuário e apresente um relatório.

O programa deverá informar:
1. Quantidade total de caracteres.
2. Quantidade de palavras.
3. Quantidade de letras maiúsculas.
4. Quantidade de letras minúsculas.
5. Quantidade de números.
6. Quantidade de espaços.
7. Quantidade de vogais.
8. Quantidade de consoantes.
9. Quantidade de ocorrências de uma palavra escolhida pelo usuário.
Você poderá utilizar len(), split(), count(), lower(), upper() e expressões regulares.
'''
texto = input('Digite um texto para análise: ')
busca = input('Digite uma palavra para busca: ')

texto_limpo = texto.strip()

comp_texto = len(texto_limpo)
qtd_carac = 0
qtd_palavras = 0
qtd_maiusculas = 0
qtd_minusculas = 0
qtd_numeros = 0
qtd_espacos = 0
qtd_vogais = 0
qtd_consoantes = 0


for i in range(comp_texto):
    if texto_limpo[i] != ' ':
        # calcula a quantidade de caracteres
        qtd_carac += 1
        # verifica se é maiúscula ou minúscula e faz a contagem
        if texto_limpo[i].isupper():
            qtd_maiusculas += 1
        else:
            qtd_minusculas += 1

        # verifica se é um número
        if texto_limpo[i].isdecimal():
            qtd_numeros += 1

        # verifica se é vogal ou consoante
        if texto_limpo[i].lower() in 'aeiou':
            qtd_vogais += 1
        elif texto_limpo[i].lower() in 'bcdfghjklmnpqrstvwxyz':
            qtd_consoantes += 1


        # verifica se chegou no final do texto
        if i == (comp_texto -1):
            qtd_palavras += 1
    else:
        qtd_palavras += 1
        qtd_espacos += 1

    # verifica a quantidade da palavra de busca
    res_busca = re.findall(busca, texto_limpo)

print(f'qtd carac: {qtd_carac}')
print(f'qtd palavras: {qtd_palavras}')
print(f'qtd maiúsculas: {qtd_maiusculas}')
print(f'qtd minúsculas: {qtd_minusculas}')
print(f'qtd números: {qtd_numeros}')
print(f'qtd espaços: {qtd_espacos}')
print(f'qtd vogais: {qtd_vogais}')
print(f'qtd consoantes: {qtd_consoantes}')
print(f'qtd palavras da busca: {len(res_busca)}')
