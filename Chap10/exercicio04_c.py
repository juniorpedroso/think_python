vendas = [
    'shake baunilha',
    'chá limão',
    'nrg original',
    'fibra de uva',
    'shake baunilha',
    'proteín powder',
    'chá Limão',
    'Shake Baunilha'
]

produtos = {}
for produto in vendas:
    produto_lower = produto.lower()
    produtos[produto_lower] = produtos.get(produto_lower, 0) + 1

for produto, qtd in produtos.items():
    print(f'{produto}: {qtd}')
