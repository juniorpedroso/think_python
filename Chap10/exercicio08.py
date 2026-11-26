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


'''

garagem = []

# motocicleta = {
#     'Modelo': None,
#     'Ano': None,
#     'Cilindrada': None,
#     'Cor': None,
#     'Quilometragem': None
# }
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
    print('Cadastro de motocicleta')
    
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
    print('Consulta de motocicleta')

# Função de atualizar quilometragem
def atualiza_quilometragem():
    print('Atualizando quilometragem')

# Função de excluir motocicleta
def exclui():
    print('Exclui motocicleta')

# Função de listar motocicleta
def listar():
    print('Lista de motocicletas')
    print('┌' + (19 * "─") + '┬' + (19 * "─") + '┬' + (19 * "─") + '┬' + (19 * "─")  + '┬' + (19 * "─") + '┐')
    # print(garagem)
    print('│',end='')
    print_palavra('Modelo')
    print_palavra('Ano')
    print_palavra('Cilindrada')
    print_palavra('Cor')
    print_palavra('Quilometragem')
    print()
    print('├' + (19 * "─") + '┼' + (19 * "─") + '┼' + (19 * "─") + '┼' + (19 * "─")  + '┼' + (19 * "─") + '┤')
    for moto in garagem:
        for chave, valor in moto.items():
            if chave == 'Modelo':
                print('│',end='')
            print_palavra(valor)
        print()
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
    