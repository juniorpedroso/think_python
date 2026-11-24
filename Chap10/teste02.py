vendas = [
    'Himalayan',
    'Meteor',
    'Himalayan',
    'Classic',
    'Himalayan',
    'Meteor',
    'Classic',
    'Himalayan'
]

contagem = {}
for modelo in vendas:
    # if modelo not in contagem:
    #     contagem[modelo] = 1
    # else:
    #     contagem[modelo] += 1
    contagem[modelo] = contagem.get(modelo, 0) + 1

print(contagem)
for chave, valor in contagem.items():
    print(f'{chave}: {valor}')