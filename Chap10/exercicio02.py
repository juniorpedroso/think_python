'''
Exercício 2 – Alterando informações
Fácil
Utilize o dicionário do exercício anterior.

Faça as seguintes operações:
1. Altere a cor de Azul para Preta.
2. Altere o ano para 2027.
3. Adicione uma nova chave chamada preco, com valor 32000.
4. Adicione uma chave chamada quilometragem, com valor 0.
5. Exclua a chave cor.
6. Imprima o resultado final.
Objetivo: praticar criação, alteração e exclusão de elementos.
'''
motocicleta = {
    'Modelo': 'Himalayan',
    'Ano': '2026',
    'Cilindrada': '450',
    'Cor': 'Azul',
    'Fabricante': 'Royal Enfield'
}

# 1. Altere a cor de azul para preta
motocicleta['Cor'] = 'preta'

# 2. Altere o ano para 2027.
motocicleta['Ano'] = '2027'

# 3. Adicione uma nova chave chamada preco, com valor 32000.
motocicleta['Preco'] = 32000

# 4. Adicione uma chave chamada quilometragem, com valor 0.
motocicleta['Quilometragem'] = 0

# 5. Exclua a chave cor.
motocicleta.pop('Cor')

# 6. Imprima o resultado final.
for chave, valor in motocicleta.items():
    print(f'{chave}: {valor}')