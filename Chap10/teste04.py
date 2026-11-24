motocicletas = [

    {
        'modelo': 'Himalayan',
        'ano': 2026,
        'preco': 29990
    },

    {
        'modelo': 'Meteor',
        'ano': 2025,
        'preco': 24990
    },

    {
        'modelo': 'Classic',
        'ano': 2026,
        'preco': 22990
    }

]


for i in range(len(motocicletas)):
    print(motocicletas[i])
for i in range(len(motocicletas)):
    for chave, valor in motocicletas[i].items():
        print(f'{chave} : {valor}')
    print('-' * 20)
