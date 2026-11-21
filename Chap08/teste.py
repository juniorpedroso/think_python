frase = 'Te quiero cada dia más'
print(frase)
print(frase.title())
print(frase.lower())
print(frase.replace('quiero', 'quero'))

for i in range(30):
    print(i % 10, end='')
print()

frase2 = 'Estou aprendendo Python'
print(frase2)
position = frase2.find('Python')
print(position)
frase2_invertida = frase2[::-1]
print(frase2_invertida)