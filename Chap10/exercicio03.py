'''
Exercício 3 – Verificando informações
Fácil
Crie este dicionário:

Agora, seu programa deverá:
1. Verificar se existe a chave modelo.
2. Verificar se existe a chave preco.
3. Verificar se o valor Himalayan existe no dicionário.
4. Utilizar get() para buscar o preço, retornando 0 caso não exista.
5. Exibir os resultados.

'''
motocicleta = {
    'modelo': 'Himalayan',
    'ano': 2026,
    'cilindrada': 450,
    'cor': 'Azul'
}

# 1. Verificar se existe a chave modelo.
print(motocicleta.get('modelo', 'Não informado'))

# 2. Verificar se existe a chave preco.
print(motocicleta.get('preco', 'Não informado'))

# 3. Verificar se o valor Himalayan existe no dicionário.
print('Himalayan'in motocicleta.values())

# 4. Utilizar get() para buscar o preço, retornando 0 caso não exista.
print(motocicleta.get('preco', 0))

# 5. Exibir os resultados.
