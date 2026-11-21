motos1 = ['meteor', 'hunter', 'classic', 'interceptor', 'Himalayan']
motos2 = motos1[3:]

for i, moto in enumerate(motos1):
    print(f'{i + 1} {moto}')
print('-' * 30)
for i, moto in enumerate(motos2):
    print(f'{i + 1} {moto}')
print('-' * 30)
print('hunter' in motos1)
print('hunter' in motos2)
motos1.sort()
print(motos1)