# def split_word(word):
#     comprimento = len(word)
#     for i in range(comprimento):
#         print(f'{i} {word[i]}')

# split_word('Python')

def split_word(word):
    for i, letra in enumerate(word, start= 1):
        print(i, letra)

split_word('Python')

palavra = 'Python'
palavra_inv = palavra[::-1]
print(palavra_inv)

texto = 'Eu estou estundando Python e Java'

soma_mai = sum(1 for c in texto if c.isupper())
soma_min = sum(1 for c in texto if c.islower())
soma_esp = sum(1 for c in texto if c == ' ')
soma_pal = len(texto.split())

print(f'soma de letras maiusculas: {soma_mai}')
print(f'soma de letras minusculas: {soma_min}')
print(f'soma de espaços: {soma_esp}')
print(f'soma de palavras: {soma_pal}')