'''
Exercício 7 – Agrupando motocicletas por categoria
Intermediário / Avançado
Considere o dicionário abaixo:
Seu objetivo é criar um dicionário que agrupe os modeloelos de acordo com suas categorias.

Resultado esperado:

Adventure: ['Himalayan', 'Scram', 'Himalayan']
Cruiser: ['Meteor', 'Super Meteor']
Classic: ['Classic', 'Goan']

Regra: utilize for, if, dicionários e listas.

Não crie manualmente as categorias no dicionário. O programa deverá identificar as categorias automaticamente.
'''
motocicletas = [
    ('Himalayan', 'Adventure'),
    ('Scram', 'Adventure'),
    ('Meteor', 'Cruiser'),
    ('Super Meteor', 'Cruiser'),
    ('Classic', 'Classic'),
    ('Goan', 'Classic'),
    ('Himalayan', 'Adventure')
]
# Cria um dicionário vazio
categorias = {}

# Loop pela lista motocicletas
for modelo, categoria in motocicletas:
    
    # Se categoria não estiver no dicionário, cria uma nova
    if categoria not in categorias:
        categorias[categoria] = []
    
    # se a categoria já existir, acrescenta o modelo
    categorias[categoria].append(modelo)

# imprime o dicionário categorias
for categoria, modelo in categorias.items():
    print(f'{categoria}: {modelo}')
