import re

texto = input('Digite um texto para análise: ')
busca = input('Digite uma palavra para busca: ')

# Contagens em uma linha cada
qtd_carac = len(texto)
qtd_palavras = len(texto.split())
qtd_maiusculas = sum(1 for c in texto if c.isupper())
qtd_minusculas = sum(1 for c in texto if c.islower())
qtd_numeros = sum(1 for c in texto if c.isdecimal())
qtd_espacos = texto.count(' ')
qtd_vogais = sum(1 for c in texto.lower() if c in 'aeiouáéíóúâêîôûãõ')
qtd_consoantes = sum(1 for c in texto.lower() if c.isalpha() and c not in 'aeiouáéíóúâêîôûãõ')
qtd_busca = len(re.findall(r'\b' + re.escape(busca) + r'\b', texto, re.IGNORECASE))

print(f'\n📊 RELATÓRIO:')
print(f'Caracteres: {qtd_carac} | Palavras: {qtd_palavras}')
print(f'Maiúsculas: {qtd_maiusculas} | Minúsculas: {qtd_minusculas}')
print(f'Números: {qtd_numeros} | Espaços: {qtd_espacos}')
print(f'Vogais: {qtd_vogais} | Consoantes: {qtd_consoantes}')
print(f'Ocorrências de "{busca}": {qtd_busca}')