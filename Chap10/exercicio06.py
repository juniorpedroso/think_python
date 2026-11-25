'''
Exercício 6 – Lista de dicionários
Intermediário
Agora vamos combinar os conhecimentos dos capítulos 9 e 10.

Crie uma lista chamada motocicletas, contendo três dicionários:

Seu programa deverá:
1. Exibir todos os modelos.
2. Exibir o preço de cada motocicleta.
3. Calcular o preço médio das três motocicletas.
4. Identificar qual motocicleta possui o maior preço.
'''
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

qtd_motos = 0
maior_preco = 0
soma_precos = 0
moto_cara = ''

# loop for para mostrar o modelo e seu valor
for moto in motocicletas:

    # verifica qual moto tem o preço mais caro
    if not moto_cara:
        moto_cara = moto['modelo']
        maior_preco = moto['preco']
    else:
        if moto['preco'] > maior_preco:
            maior_preco = moto['preco']
            moto_cara = moto['modelo']
    # acumula a quantidade motos
    qtd_motos += 1
    # soma o preço de todas as motos
    soma_precos += moto['preco']
    print(f'{moto['modelo']} - R$ {moto['preco']}')

# calcula o preço médio das motos
preco_medio = int(soma_precos / qtd_motos)
print()
print(f'Preço médio: R$ {preco_medio}')
print(f'Maior preço: R$ {moto_cara}')
