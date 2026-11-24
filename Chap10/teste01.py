motocicleta = {
    'modelo': 'Himalayan',
    'ano': 2026,
    'cilindrada': 450,
    'cor': 'Azul',
    'preco': 29990.00
}

print(motocicleta)

pessoa = {}
pessoa['nome'] = 'Carlos'
pessoa['idade'] = 35
pessoa['cidade'] = 'São Paulo'

print(pessoa)

print(motocicleta['modelo'])
print(motocicleta['ano'])
print(motocicleta['cilindrada'])

motocicleta['cor'] = 'preta'

print(motocicleta)

motocicleta['placa'] = 'UQQ1F75'

print(motocicleta)
del(motocicleta['cor'])
motocicleta.pop('ano')
print(motocicleta)
print('Himalayan' in motocicleta.values())