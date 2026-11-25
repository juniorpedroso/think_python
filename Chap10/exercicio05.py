'''
Exercício 5 – Percorrendo um dicionário
Intermediário
Crie o dicionário abaixo:

Seu programa deverá:
1. Imprimir todas as chaves.
2. Imprimir todos os valores.
3. Imprimir as chaves e valores juntos.
4. Utilizar uma f-string para formatar a saída.

Exemplo de resultado:
Modelo: Himalayan
Ano: 2026
Cilindrada: 450
Potência: 40
Cor: Azul
Fabricante: Royal Enfield
'''
motocicleta = {
    'modelo': 'Himalayan',
    'ano': 2026,
    'cilindrada': 450,
    'potencia': 40,
    'cor': 'Azul',
    'fabricante': 'Royal Enfield'
}

# 1. Imprimir todas as chaves.
print('-' * 30)
for chave in motocicleta.keys():
    print(chave)

# 2. Imprimir todos os valores.
print('-' * 30)
for valor in motocicleta.values():
    print(valor)

# 3. Imprimir as chaves e valores juntos.
print('-' * 30)
for chave, valor in motocicleta.items():
    print(f'{chave}: {valor}')
