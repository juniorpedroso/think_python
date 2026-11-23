'''
Exercício 8 – Desafio: Sistema de gerenciamento de motocicletas
Desafio intermediário
Objetivo: reunir vários conceitos do capítulo em um único programa.

Vamos criar um pequeno sistema para gerenciar uma lista de motocicletas.

Comece com:
motos = ['Himalayan', 'Scram', 'Interceptor']

Seu programa deverá oferecer as seguintes funcionalidades:
1. Mostrar todas as motocicletas cadastradas.
2. Adicionar uma nova motocicleta.
3. Remover uma motocicleta pelo nome.
4. Verificar se determinada motocicleta está cadastrada.
5. Mostrar a quantidade de motocicletas.
6. Ordenar os nomes alfabeticamente.
7. Encerrar o programa quando o usuário desejar.

Sugestão de funcionamento:

===== GERENCIADOR DE MOTOS =====

1 - Listar motocicletas
2 - Adicionar motocicleta
3 - Remover motocicleta
4 - Pesquisar motocicleta
5 - Quantidade de motocicletas
6 - Ordenar motocicletas
0 - Sair

Escolha uma opção:

- Utilize while para manter o programa funcionando.
- Utilize if, elif e else para tratar as opções.
- Utilize append() para adicionar.
- Utilize remove() para remover.
- Utilize in para pesquisar.
- Utilize len() para contar.
- Utilize sort() para ordenar.
Este exercício é particularmente interessante porque começa a aproximar os conhecimentos estudados de um programa real.
'''
motos = ['Himalayan', 'Scram', 'Interceptor']
opcao = 1

# Função para imprimir menu
def menu():
    print('''===== GERENCIADOR DE MOTOS =====
1 - Listar motocicletas
2 - Adicionar motocicleta
3 - Remover motocicleta
4 - Pesquisar motocicleta
5 - Quantidade de motocicletas
6 - Ordenar motocicletas
0 - Sair''')
    return int(input('Escolha uma opção: '))


# Função para listar motos
def listar_motos():
    print('Lista de motos')
    print('-' * 32)
    for i, moto in enumerate(motos):
        print(f'{i+ 1}  {moto}')
    print('-' * 30)

# Função para adicionar motos
def adic_moto():
    # solicita o nome da nova moto
    nova_moto = input('Digite a nova moto: ').strip()
    # se deixou um espaço em branco, avisa
    if not nova_moto:
        print('Nome inválido!!!')
    # se a nova moto já está cadastrada, emite um aviso
    elif nova_moto in motos:
        print('Esta moto já está cadastrada.')
    # cadastra a nova moto
    else:
        motos.append(nova_moto)
        print(f'{nova_moto} foi cadastrada.')

# Função para remover moto
def remov_moto():
    moto_a_remov = input('Digite a moto para remover: ').strip()
    if not moto_a_remov:
        print('Nome inválido!!!')
    elif moto_a_remov in motos:
        motos.remove(moto_a_remov)
        print(f'{moto_a_remov} foi removida!')
    else:
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
    print('Nova')
    listar_motos()


# Loop principal
while opcao != 0:
    opcao = menu()

    # listar motos
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

    # Qtd de motos
    elif opcao == 5:
        print(f'Quantidade de motocicletas: {len(motos)}')

    # Ordenar motos
    elif opcao == 6:
        ord_motos()

    # Sair
    elif opcao == 0:
        print('Saindo.....')
