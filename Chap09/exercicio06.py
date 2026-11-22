'''
Exercício 6 – Identificando palíndromos
Intermediário
Objetivo: combinar os conhecimentos dos capítulos 8 e 9.

Crie uma lista:
palavras = ['radar', 'python', 'arara', 'casa', 'ovo', 'osso', 'moto']

Seu programa deverá:
1. Percorrer a lista utilizando for.
2. Verificar se cada palavra é um palíndromo.
3. Imprimir somente as palavras que são palíndromos.
4. Contar quantos palíndromos foram encontrados.

Dica: compare cada palavra com palavra[::-1].
'''
palavras = ['radar', 'python', 'arara', 'casa', 'ovo', 'osso', 'moto']

# função parara verficar se é palíndromo
def eh_palindromo(palavra):
    return palavra == palavra[::-1]

# percorrer a lista utilizando for, 
# verificar se cada palavra é um palíndromo e imprimi-la
# contar quantas palíndromos são.
qtd_palindromos = 0
for palavra in palavras:
    if eh_palindromo(palavra):
        print(f'A palavra {palavra} é palíndromo')
        qtd_palindromos += 1
print(f'Foram encontrados {qtd_palindromos} palíndromos')
