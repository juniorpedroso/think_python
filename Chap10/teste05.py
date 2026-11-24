vendas = [
    ('Himalayan', 'Adventure'),
    ('Meteor', 'Cruiser'),
    ('Classic', 'Classic'),
    ('Himalayan', 'Adventure'),
    ('Meteor', 'Cruiser')
]

categorias = {}

for modelo, categoria in vendas:

    if categoria not in categorias:
        categorias[categoria] = []

    categorias[categoria].append(modelo)

print(categorias)