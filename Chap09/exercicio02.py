'''
Exercício 2 – Modificando elementos
Fácil
Objetivo: praticar a mutabilidade das listas.

Crie a seguinte lista:
numeros = [10, 20, 30, 40, 50]

Seu programa deverá:
1. Substituir o primeiro elemento por 100.
2. Substituir o terceiro elemento por 300.
3. Substituir o último elemento por 500.
4. Imprimir a lista modificada.
'''
numeros = [10, 20, 30, 40, 50]
numeros[0] = 100
numeros[2] = 300
numeros[-1] = 500
print(numeros)
