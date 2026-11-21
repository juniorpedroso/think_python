import re

texto = input('Digite um texto para análise: ')
busca = input('Digite uma palavra para busca: ')

# 1. Quantidade total de caracteres (incluindo espaços)
qtd_carac = len(texto)

# 2. Quantidade de palavras (usando split, que é mais confiável)
palavras = texto.split()
qtd_palavras = len(palavras)

# 3-8. Contagens usando loops e métodos de string
qtd_maiusculas = 0
qtd_minusculas = 0
qtd_numeros = 0
qtd_espacos = 0
qtd_vogais = 0
qtd_consoantes = 0

for caractere in texto:
    if caractere.isupper():
        qtd_maiusculas += 1
    elif caractere.islower():
        qtd_minusculas += 1
    
    if caractere.isdecimal():
        qtd_numeros += 1
    
    if caractere == ' ':
        qtd_espacos += 1
    
    caractere_lower = caractere.lower()
    if caractere_lower in 'aeiouáéíóúâêîôûãõ':  # Inclui acentos
        qtd_vogais += 1
    elif caractere_lower in 'bcdfghjklmnpqrstvwxyz':
        qtd_consoantes += 1

# 9. Quantidade de ocorrências da palavra buscada (FORA do loop!)
res_busca = re.findall(r'\b' + re.escape(busca) + r'\b', texto, re.IGNORECASE)
qtd_busca = len(res_busca)

# Exibição dos resultados
print(f'\n📊 RELATÓRIO DE ANÁLISE:')
print(f'Qtd caracteres: {qtd_carac}')
print(f'Qtd palavras: {qtd_palavras}')
print(f'Qtd maiúsculas: {qtd_maiusculas}')
print(f'Qtd minúsculas: {qtd_minusculas}')
print(f'Qtd números: {qtd_numeros}')
print(f'Qtd espaços: {qtd_espacos}')
print(f'Qtd vogais: {qtd_vogais}')
print(f'Qtd consoantes: {qtd_consoantes}')
print(f'Qtd ocorrências de "{busca}": {qtd_busca}')