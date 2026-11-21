# motos = ['Himalayan', 'Scram', 'Interceptor', 'Meteor', 'Classic']
# for i, moto in enumerate(motos, start = 1):
#     print(f'{i} {moto}')

# print(motos[2:])
# print(motos[-3:])

motos = [['Himalaian', '450', 29990], ['Bear', '650', 33990], ['Meteor', '350', 24990], 
               ['Guerrilla', '450', 29490], ['Hunter', '350', 19990], ['Classic', '350', 23990]]
print(motos)

modelos_350 = sum(1 for cc in motos if cc[1] == '350')

print(modelos_350)
# preco_total = 0
# for moto in motos:
#     preco_total += moto[2]

# preco_total = sum(moto[2] for moto in motos)
preco_total = sum(preco for nome, cilindrade, preco in motos)

print(preco_total)