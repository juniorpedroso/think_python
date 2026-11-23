'''
Abaixo está uma versão revisada do seu programa. Mantive sua estrutura original, seus nomes de funções e a lógica que você desenvolveu. 
Fiz apenas os ajustes necessários.
'''

motos = ['Himalayan', 'Scram', 'Interceptor']


# Função para imprimir menu
def menu():
    print('''
===== GERENCIADOR DE MOTOS =====

1 - Listar motocicletas
2 - Adicionar motocicleta
3 - Remover motocicleta
4 - Pesquisar motocicleta
5 - Quantidade de motocicletas
6 - Ordenar motocicletas
0 - Sair
''')

    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite somente números!')
        return -1


# Função para listar motos
def listar_motos():
    print('\nLista de motos')
    print('-' * 32)

    if not motos:
        print('Nenhuma motocicleta cadastrada.')
    else:
        for i, moto in enumerate(motos, start=1):
            print(f'{i} - {moto}')

    print('-' * 32)


# Função para adicionar motos
def adic_moto():
    nova_moto = input('Digite a nova moto: ').strip()

    if not nova_moto:
        print('Nome inválido!!!')

    elif nova_moto.lower() in [moto.lower() for moto in motos]:
        print('Esta moto já está cadastrada.')

    else:
        motos.append(nova_moto)
        print(f'{nova_moto} foi cadastrada.')


# Função para remover moto
def remov_moto():
    moto_a_remov = input('Digite a moto para remover: ').strip()

    if not moto_a_remov:
        print('Nome inválido!!!')
        return

    for moto in motos:
        if moto.lower() == moto_a_remov.lower():
            motos.remove(moto)
            print(f'{moto} foi removida!')
            return

    print(f'{moto_a_remov} não está cadastrada.')


# Função para pesquisar moto
def pesq_moto():
    moto_a_pesq = input('Digite a moto para pesquisar: ').strip()

    if not moto_a_pesq:
        print('Nome inválido!!!')

    elif moto_a_pesq.lower() in [moto.lower() for moto in motos]:
        print(f'{moto_a_pesq} está cadastrada na lista.')

    else:
        print(f'{moto_a_pesq} não está cadastrada na lista.')


# Função para ordenar motos
def ord_motos():
    motos.sort(key=str.lower)
    print('Lista ordenada alfabeticamente:')
    listar_motos()


# Loop principal
while True:

    opcao = menu()

    # Listar motos
    if opcao == 1:
        listar_motos()

    # Cadastrar motos
    elif opcao == 2:
        adic_moto()

    # Remover moto
    elif opcao == 3:
        remov_moto()

    # Pesquisar moto
    elif opcao == 4:
        pesq_moto()

    # Quantidade de motos
    elif opcao == 5:
        print(f'Quantidade de motocicletas: {len(motos)}')

    # Ordenar motos
    elif opcao == 6:
        ord_motos()

    # Sair
    elif opcao == 0:
        print('Encerrando o programa...')
        break

    # Opção inválida
    else:
        print('Opção inválida! Tente novamente.')

