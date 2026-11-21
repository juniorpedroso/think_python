'''
Exercício 3 – Utilizando métodos de listas
Fácil / intermediário
Objetivo: praticar append(), extend(), insert(), remove() e pop().

Comece com:
frutas = ['Maçã', 'Banana', 'Laranja']

Seu programa deverá executar as seguintes operações, nesta ordem:
1. Adicionar Uva ao final da lista.
2. Adicionar Abacaxi e Melancia utilizando extend().
3. Inserir Morango na posição 1.
4. Remover Banana.
5. Remover o último elemento utilizando pop().
6. Imprimir a lista final.
7. Imprimir o elemento removido pelo pop().
Dica: utilize os métodos na ordem solicitada e observe como a lista muda a cada operação.
'''

frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
frutas.append('Uva')
print(frutas)
frutas.extend(['Abacaxi', 'Melancia'])
print(frutas)
frutas.insert(1, 'Morango')
print(frutas)
frutas.remove('Banana')
print(frutas)
fruta_removida = frutas.pop()
print(frutas)
print(f'Fruta removida = {fruta_removida}')
