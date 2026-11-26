'''
Exercício 8 – Desafio: Sistema de gerenciamento de motocicletas
Desafio
Este exercício será o mais completo da aula.

Você deverá criar um pequeno sistema de gerenciamento de motocicletas utilizando dicionários e listas.

O programa deverá começar com um dicionário vazio:
garagem = {}

Cada motocicleta deverá possuir:
- Modelo;
- Ano;
- Cilindrada;
- Cor;
- Quilometragem.
O sistema deverá permitir:
1. Cadastrar uma motocicleta.
2. Consultar uma motocicleta pelo modelo.
3. Alterar a quilometragem.
4. Excluir uma motocicleta.
5. Listar todas as motocicletas cadastradas.
6. Encerrar o programa.
Exemplo de como deverá funcionar:

===== SISTEMA DE GARAGEM =====

1 - Cadastrar motocicleta
2 - Consultar motocicleta
3 - Atualizar quilometragem
4 - Excluir motocicleta
5 - Listar motocicletas
6 - Sair

Escolha uma opção:
-----------------------
Exemplo de Cadastro:
Modelo: Himalayan
Ano: 2026
Cilindrada: 450
Cor: Azul
Quilometragem: 1500

Motocicleta cadastrada com sucesso!
-----------------------
Dicas para desenvolver:
- Utilize while para manter o menu funcionando.
- Utilize if, elif e else para controlar as opções.
- Utilize input() para receber informações.
- Utilize dicionários para armazenar os dados.
- Utilize funções para organizar o código.
- Utilize get() para evitar erros ao consultar informações inexistentes.
Não se preocupe se não conseguir concluir esse exercício de primeira. Ele foi pensado para exigir que você combine vários conhecimentos.



garagem = [
    {
        'Modelo': 'Himalayan',
        'Ano': '2026',
        'Cilindrada': '450',
        'Cor': 'preta',
        'Quilometragem': '3000'
    },
    {
        'Modelo': 'Interceptor',
        'Ano': '2025',
        'Cilindrada': '650',
        'Cor': 'preta',
        'Quilometragem': '6000'
    },
    {
        'Modelo': 'GS 1250',
        'Ano': '2023',
        'Cilindrada': '1250',
        'Cor': 'branca',
        'Quilometragem': '9000'
    },
    {
        'Modelo': 'Tiger',
        'Ano': '2022',
        'Cilindrada': '900',
        'Cor': 'verde',
        'Quilometragem': '19000'
    }
]
'''
garagem = []

opcao = 1

# função para alinhamento de palavra sendo que o máximo do tamanho da palavra será de 18
def print_palavra(palavra):
    tam_palavra = len(palavra)
    if tam_palavra > 18:
        nova_palavra = palavra[:18]
        print(f' {nova_palavra}│', end='')
    else:
        margem = (18 - tam_palavra) * ' '
        print(f' {palavra}{margem}│',end='')


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
    # return int(input('Escolha uma opção: '))
    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite somente números!')
        return -1


# Função de cadastro de motocicleta
def cadastro():
    motocicleta = {}
    print('<< CADASTRO DE MOTOCICLETA >>')
    
    # recebendo os valores das variáveis
    modelo = input('Modelo: ')
    ano = input('Ano: ')
    cilindrada = input('Cilindrada: ')
    cor = input('Cor: ')
    quilometragem = input('Quilometragem: ')

    # salvando os valores no dicionário
    motocicleta['Modelo'] = modelo
    motocicleta['Ano'] = ano
    motocicleta['Cilindrada'] = cilindrada
    motocicleta['Cor'] = cor
    motocicleta['Quilometragem'] = quilometragem

    # salvando o dicionário na lista
    garagem.append(motocicleta)
    print(f'Motocicleta {modelo} cadastrada com sucesso!')

    

# Função de Consulta de motocicleta
def consulta():
    print('<< CONSULTA DE MOTOCICLETA >>')

    # verifica se há motocicletas cadastradas
    if len(garagem) == 0:
        print('Não há motocicletas cadastradas!')
        return

    # recebe a moto para consultar
    moto_a_pesq = input('Digite a moto para pesquisar: ').strip()

    # verifica se foi digitado um nome válido
    if not moto_a_pesq:
        print('Nome inválido!')
        return

    # inicial um loop pela lista garagem
    for moto in garagem:
        if moto_a_pesq.lower() == moto['Modelo'].lower():
            print(f'A motocicleta {moto_a_pesq} está cadastrada.')
            return
    print(f'A motocicleta {moto_a_pesq} não está cadastrada.')


# Função de atualizar quilometragem
def atualiza_quilometragem():
    print('<< ATUALIZAÇÃO DE QUILOMETRAGEM >>')

    # verifica se há motocicletas cadastradas
    if len(garagem) == 0:
        print('Não há motocicletas cadastradas!')
        return

    # recebe o nome da moto para atualizar
    moto_a_atualizar = input('Digite a moto para atualizar: ').strip()

    # verifica se foi digitado nome válido
    if not moto_a_atualizar:
        print('Nome inválido!')
        return

    # inicia um loop pela lista garagem
    for moto in garagem:
        if moto_a_atualizar.lower() == moto['Modelo'].lower():
            # se a moto estiver cadastrada solicita uma nova quilometragem
            km_atual = input('Digite a nova quilometragem: ')
            if not km_atual.isnumeric():
                print('Digite somente números!')
                return
            
            # verifica se o km informado é igual ou menor que o que está cadastrado
            elif int(km_atual) == int(moto['Quilometragem']):
                print('A quilometragem digitada é a mesma cadastrada. Não foi alterado!')
                return
            elif int(km_atual) < int(moto['Quilometragem']):
                print('A quilometragem digitada é menor que a cadastrada. Não foi alterado!')
                return
            
            # atualiza a quilomentragem
            else:
                moto['Quilometragem'] = km_atual
                print('Quilometragem atualizada!')
                return
    
    print(f'Motocicleta {moto_a_atualizar} não cadastrada!')

# Função de excluir motocicleta
def exclui():
    print('<< EXCLUSÃO DE MOTOCICLETA >>')

    # verifica se a lista garagem está vazia
    if len(garagem) == 0:
        print('Não há motocicletas cadastradas!')
        return
    
    # recebe a motocicleta para excluir
    moto_a_excluir = input('Digite a moto para excluir: ').strip()
    if not moto_a_excluir:
        print('Nome inválido!')
        return

    # inicia um loop pela lista garagem
    for moto in garagem:
        if moto_a_excluir.lower() == moto['Modelo'].lower():

            # solicita confirmação para excluir a motocicleta
            confirma = input(f'Confirma que quer excluir {moto_a_excluir}? S/N: ')
            if confirma in 'Ss':
                
                # remove a motocicleta
                garagem.remove(moto)
                print(f'A motocicleta {moto_a_excluir} foi excluída!.')
                return
            else:
                print(f'A motocicleta {moto_a_excluir} NÃO foi excluída!.')
                return
            
    print(f'A motocicleta {moto_a_excluir} não está cadastrada.')



# Função de listar motocicleta
def listar():
    print('<< LISTA DE MOTOCICLETAS >>')

    # verifica se há motocicletas cadastradas
    if len(garagem) == 0:
        print('Não há motocicletas cadastradas!')
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
        for chave, valor in moto.items():

            # print dos dados das motocicletas
            if chave == 'Modelo':
                print('│',end='')
            print_palavra(valor)
        print()
    # desenha a borda inferior da lista
    print('└' + (19 * "─") + '┴' + (19 * "─") + '┴' + (19 * "─") + '┴' + (19 * "─")  + '┴' + (19 * "─") + '┘')

# loop principal
while opcao != 6:
    opcao = menu()

    # Cadastrar motocicleta
    if opcao == 1:
        cadastro()

    # Consulta de motocicleta
    elif opcao == 2:
        consulta()

    # Atualização de quilometragem
    elif opcao == 3:
        atualiza_quilometragem()

    # Exclui motocicleta
    elif opcao == 4:
        exclui()

    # Listar motocicleta
    elif opcao == 5:
        listar()

    # Sair do programa
    elif opcao == 6:
        print('Saindo....')
    