vendas = [
    'Himalayan',
    'Meteor',
    'Classic',
    'Himalayan',
    'Himalayan',
    'Meteor',
    'Classic',
    'Himalayan',
    'Meteor',
    'Himalayan'
]

def analisar_vendas(vendas):
    """Analisa e exibe relatório de vendas de motocicletas"""
    modelos = {}
    for modelo in vendas:
        modelos[modelo] = modelos.get(modelo, 0) + 1
    
    total = sum(modelos.values())
    
    print("🏍️  RELATÓRIO DE VENDAS")
    print("=" * 40)
    
    for modelo, qtd in sorted(modelos.items(), key=lambda x: x[1], reverse=True):
        percentual = (qtd / total) * 100
        barra = "█" * int(percentual / 2)  # Gráfico de barras
        print(f'{modelo:12} | {qtd:2} | {percentual:5.1f}% | {barra}')
    
    print("=" * 40)
    print(f'Total de vendas: {total}')
    print(f'Modelo mais vendido: {max(modelos, key=modelos.get)}')

analisar_vendas(vendas)