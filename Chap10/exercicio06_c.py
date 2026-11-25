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

soma_precos = 0
moto_cara = None
moto_barata = None

# loop for para mostrar o modelo e seu valor
for moto in motocicletas:

    # verifica qual motocicleta possui o maior preço
    if moto_cara is None or moto['preco'] > moto_cara['preco']:
        moto_cara = moto
    
    # verifica qual motocicleta possui o menor preço
    if moto_barata is None or moto['preco'] < moto_barata['preco']:
        moto_barata = moto
    
    # soma o preço de todas as motos
    soma_precos += moto['preco']
    print(f'{moto['modelo']} - R$ {moto['preco']:.2f}')

# calcula o preço médio das motos
preco_medio = (soma_precos / len(motocicletas))
print()
print(f'Preço médio: R$ {preco_medio:.2f}')
print()
print(f'Motocicleta mais cara: {moto_cara['modelo']}')
print(f'Maior preço: R$ {moto_cara['preco']:.2f}')
print()
print(f'Motocicleta mais barata: {moto_barata['modelo']}')
print(f'Menor preço: R$ {moto_barata['preco']:.2f}')
