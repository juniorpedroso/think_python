pessoas = [
    {
        'nome': 'Junior',
        'idade': 55,
        'cidade': 'Avaré'
    },
    {
        'nome': 'Daniele',
        'idade': 51,
        'cidade': 'Avaré'
    },
    {
        'nome': 'Igor',
        'idade': 30,
        'cidade': 'São Paulo'
    },
    {  
        'nome': 'Hugo',
        'idade': 28,
        'cidade': 'Sorocaba'
    },

]

for pessoa in pessoas:
    for chave, valor in pessoa.items():
        print(f'{chave}, {valor}')
    print('-' * 30)

for pessoa in pessoas:
    print(f'Nome: {pessoa['nome']}, idade: {pessoa['idade']}, cidade: {pessoa['cidade']}')