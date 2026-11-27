'''
Exercício 8 – Desafio: Sistema de gerenciamento de motocicletas

'''
garagem = []

opcao = 1

# função para alinhamento de palavra sendo que o máximo do tamanho da palavra será de 18
def print_palavra(palavra):
    print(f' {str(palavra)[:18].ljust(18)}│', end='')

# Função para verificar se a lista garagem está vazia
def garagem_vazia():
    if not garagem:
        print('Não há motocicletas cadastradas!')
        return True
    return False

def menu():
    print('''
===== SISTEMA DE GARAGEM =====

1 - Cadastrar motocicleta
2 - Consultar motocicleta
3 - Atualizar quilometragem
4 - Excluir motocicleta
5 - Listar motocicletas
6 - Sair
''')
    
    try:
        opcao =int(input('Escolha uma opção: '))

        if 1 <= opcao <= 6:
            return opcao

        print('Opcão inválida!')
        return -1
    
    except ValueError:
        print('Digite somente números!')
        return -1


# Função de cadastro de motocicleta
def cadastro(garagem):
    motocicleta = {}
    print('<< CADASTRO DE MOTOCICLETA >>')
    
    # recebendo os valores das variáveis
    modelo = input('Modelo: ').strip()

    # verificar se a motocicleta já não está cadastrada
    for moto in garagem:
        if moto['modelo'].lower() == modelo.lower():
            print('Essa motocicleta já está cadastrada!')
            return

    ano = int(input('Ano: '))
    cilindrada = int(input('Cilindrada: '))
    cor = input('Cor: ')
    quilometragem = int(input('Quilometragem: '))

    # salvando os valores no dicionário
    motocicleta['modelo'] = modelo
    motocicleta['ano'] = ano
    motocicleta['cilindrada'] = cilindrada
    motocicleta['cor'] = cor
    motocicleta['quilometragem'] = quilometragem

    # salvando o dicionário na lista
    garagem.append(motocicleta)
    print(f'Motocicleta {modelo} cadastrada com sucesso!')

    

# Função de Consulta de motocicleta
def consulta(garagem):
    print('<< CONSULTA DE MOTOCICLETA >>')

    # verifica se há motocicletas cadastradas
    if garagem_vazia():
        return

    # recebe a moto para consultar
    moto_a_pesq = input('Digite a moto para pesquisar: ').strip()

    # verifica se foi digitado um nome válido
    if not moto_a_pesq:
        print('Nome inválido!')
        return

    # inicial um loop pela lista garagem
    for moto in garagem:
        if moto_a_pesq.lower() == moto['modelo'].lower():
            print(f'A motocicleta {moto_a_pesq} está cadastrada.')

            # print da motocicleta cadastrada
            for chave, valor in moto.items():
                print(f'{chave}: {valor}')
            return
    print(f'A motocicleta {moto_a_pesq} não está cadastrada.')


# Função de atualizar quilometragem
def atualiza_quilometragem(garagem):
    print('<< ATUALIZAÇÃO DE QUILOMETRAGEM >>')

    # verifica se há motocicletas cadastradas
    if garagem_vazia():
        return

    # recebe o nome da moto para atualizar
    moto_a_atualizar = input('Digite a moto para atualizar: ').strip()

    # verifica se foi digitado nome válido
    if not moto_a_atualizar:
        print('Nome inválido!')
        return

    # inicia um loop pela lista garagem
    for moto in garagem:
        if moto_a_atualizar.lower() == moto['modelo'].lower():
            # se a moto estiver cadastrada solicita uma nova quilometragem
            km_atual = input('Digite a nova quilometragem: ')
            if not km_atual.isdigit() or int(km_atual) < 0:
                print('Digite uma quilometragem válida!')
                return
            
            # verifica se o km informado é igual ou menor que o que está cadastrado
            elif int(km_atual) == moto['quilometragem']:
                print('A quilometragem digitada é a mesma cadastrada. Não foi alterado!')
                return
            elif int(km_atual) < moto['quilometragem']:
                print('A quilometragem digitada é menor que a cadastrada. Não foi alterado!')
                return
            
            # atualiza a quilomentragem
            else:
                moto['quilometragem'] = int(km_atual)
                print('Quilometragem atualizada!')
                return
    
    print(f'Motocicleta {moto_a_atualizar} não cadastrada!')

# Função de excluir motocicleta
def exclui(garagem):
    print('<< EXCLUSÃO DE MOTOCICLETA >>')

    # verifica se a lista garagem está vazia
    if garagem_vazia():
        return
    
    # recebe a motocicleta para excluir
    moto_a_excluir = input('Digite a moto para excluir: ').strip()
    if not moto_a_excluir:
        print('Nome inválido!')
        return

    # inicia um loop pela lista garagem
    for moto in garagem:
        if moto_a_excluir.lower() == moto['modelo'].lower():

            # solicita confirmação para excluir a motocicleta
            confirma = input(f'Confirma que quer excluir {moto_a_excluir}? S/N: ').strip().lower()
            if confirma in 's':
                # remove a motocicleta
                garagem.remove(moto)
                print(f'A motocicleta {moto_a_excluir} foi excluída!.')
                return
            else:
                print(f'A motocicleta {moto_a_excluir} NÃO foi excluída!.')
                return
            
    print(f'A motocicleta {moto_a_excluir} não está cadastrada.')



# Função de listar motocicleta
def listar(garagem):
    print('<< LISTA DE MOTOCICLETAS >>')

    # verifica se há motocicletas cadastradas
    if garagem_vazia():
        return   
    
    # Desenha a borda superior da lista
    print('┌' + (19 * "─") + '┬' + (19 * "─") + '┬' + (19 * "─") + '┬' + (19 * "─")  + '┬' + (19 * "─") + '┐')
    # print o menu da lista
    print('│',end='')
    print_palavra('Modelo')
    print_palavra('Ano')
    print_palavra('Cilindrada')
    print_palavra('Cor')
    print_palavra('Quilometragem')
    print()
    # desenha a borda do meio da lista
    print('├' + (19 * "─") + '┼' + (19 * "─") + '┼' + (19 * "─") + '┼' + (19 * "─")  + '┼' + (19 * "─") + '┤')

    # inicia um loop pela lista garagem
    for moto in garagem:
        print('│',end='')
        for chave in ['modelo', 'ano', 'cilindrada', 'cor', 'quilometragem']:
            print_palavra(str(moto[chave]))
        print()

    # desenha a borda inferior da lista
    print('└' + (19 * "─") + '┴' + (19 * "─") + '┴' + (19 * "─") + '┴' + (19 * "─")  + '┴' + (19 * "─") + '┘')

# loop principal
while opcao != 6:
    opcao = menu()

    # Cadastrar motocicleta
    if opcao == 1:
        cadastro(garagem)

    # Consulta de motocicleta
    elif opcao == 2:
        consulta(garagem)

    # Atualização de quilometragem
    elif opcao == 3:
        atualiza_quilometragem(garagem)

    # Exclui motocicleta
    elif opcao == 4:
        exclui(garagem)

    # Listar motocicleta
    elif opcao == 5:
        listar(garagem)

    # Sair do programa
    elif opcao == 6:
        print('Saindo....')
    