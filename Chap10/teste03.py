concessionaria = {
    'modelos': ['Himalayan', 'Meteor', 'Classic'],
    'vendedor': 'Carlos',
    'cidade': 'São Paulo'
}

print(concessionaria['modelos'])

for chave, valor in concessionaria.items():
    print(f'{chave} : {valor}' )

