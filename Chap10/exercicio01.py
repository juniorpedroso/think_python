'''
Exercício 1 – Criando seu primeiro dicionário
Fácil
Crie um dicionário chamado motocicleta com as seguintes informações:
- Modelo: Himalayan
- Ano: 2026
- Cilindrada: 450
- Cor: Azul
- Fabricante: Royal Enfield
Depois:
1. Imprima o dicionário completo.
2. Imprima somente o modelo.
3. Imprima somente o ano.
4. Imprima a cilindrada utilizando uma f-string.
'''
motocicleta = {
    'Modelo': 'Himalayan',
    'Ano': '2026',
    'Cilindrada': '450',
    'Cor': 'Azul',
    'Fabricante': 'Royal Enfield'
}

# Imprima o dicionário completo
print(motocicleta)

# Imprima somente o modelo
print(f'Modelo: {motocicleta['Modelo']}')

# Imprima somente o ano
print(f'Ano: {motocicleta['Ano']}')

# Imprima a cilindrada utilizando uma f-string
print(f'Cilindrada: {motocicleta['Cilindrada']} cc')
