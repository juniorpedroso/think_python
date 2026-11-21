def palindromo(palavra):
    return palavra == palavra[::-1]

palavras = ['radar', 'python', 'arara', 'casa', 'ovo', 'moto']

for palavra in palavras:
    print(f'palavra {palavra} é palíndromo? {palindromo(palavra)}')
    
