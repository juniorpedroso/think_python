'''
Exercício 1 – Criando e acessando listas
Fácil
Objetivo: praticar a criação de listas e o acesso aos elementos através dos índices.

Crie uma lista chamada motos contendo cinco modelos de motocicletas.

Seu programa deverá:
1. Imprimir a lista completa.
2. Imprimir o primeiro elemento.
3. Imprimir o terceiro elemento.
4. Imprimir o último elemento utilizando índice negativo.
5. Mostrar quantos elementos existem na lista utilizando len().
'''

motos = ['Himalayan', 'Meteor', 'Hunter', 'Scram', 'Guerrilla']
print(motos)
print()

print(f'Primeira moto: {motos[0]}')

print(f'Terceira moto: {motos[2]}')

print(f'Última moto: {motos[-1]}')

print(f'Quantidade de motos: {len(motos)}')
