'''
Exercício 4 – Contador de motocicletas
Intermediário
Considere a lista abaixo:
Crie um programa que conte quantas vezes cada modelo aparece.
Resultado esperado:
Himalayan: 5
Meteor: 3
Classic: 2

Desafio adicional: faça o programa funcionar sem utilizar o método count() das listas.

Utilize um dicionário e um laço for.
'''
vendas = [
    'Himalayan',
    'Meteor',
    'Classic',
    'Himalayan',
    'Himalayan',
    'Meteor',
    'Classic',
    'Himalayan',
    'Meteor',
    'Himalayan'
]

modelos = {}
for modelo in vendas:
    modelos[modelo] = modelos.get(modelo, 0) + 1

for modelo, qtd in modelos.items():
    print(f'{modelo}: {qtd}')
