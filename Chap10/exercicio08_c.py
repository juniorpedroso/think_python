'''
Exercício 8 – Desafio: Sistema de gerenciamento de motocicletas

'''
garagem = []

# opcao = 1


# Formata uma palavra para caber em 18 caracteres na tabela
def print_palavra(palavra):
    print(f' {str(palavra)[:18].ljust(18)}│', end='')

# Função para verificar se a lista garagem está vazia
def garagem_vazia():
    if not garagem:
        print('❌ Não há motocicletas cadastradas!')
        return True
    return False

# Função auxiliar para validar entrada numérica
def input_numero(mensagem, minimo=0, maximo=None):
    """Função auxiliar para validar entrada numérica"""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f'❌ Valor deve ser maior ou igual a {minimo}!')
                continue
            if maximo and valor > maximo:
                print(f'❌ Valor deve ser menor ou igual a {maximo}!')
                continue
            return valor
        except ValueError:
            print('❌ Digite um número válido!')


def menu():
    print('''
╔══════════════════════════════════╗
║   🏍️  SISTEMA DE GARAGEM  🏍️    ║
╠══════════════════════════════════╣
║  1 - Cadastrar motocicleta       ║
║  2 - Consultar motocicleta       ║
║  3 - Atualizar quilometragem     ║
║  4 - Excluir motocicleta         ║
║  5 - Listar motocicletas         ║
║  6 - Sair                        ║
╚══════════════════════════════════╝    
''')
    
    try:
        opcao =int(input('Escolha uma opção: '))

        if 1 <= opcao <= 6:
            return opcao

        print('❌ Opcão inválida!')
        return -1
    
    except ValueError:
        print('❌ Digite somente números!')
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
            print(f'❌ A motocicleta {modelo} já está cadastrada!')
            return

    # Validação de todos os campos numéricos
    ano = input_numero('Ano: ', minimo=1900, maximo=2030)
    cilindrada = input_numero('Cilindrada: ', minimo=50)
    cor = input('Cor: ').strip()
    quilometragem = input_numero('Quilometragem: ', minimo=0)

    # criar e salvar a motocicleta
    motocicleta = {
        'modelo': modelo,
        'ano': ano,
        'cilindrada': cilindrada,
        'cor': cor,
        'quilometragem': quilometragem
    }

    # salvando o dicionário na lista
    garagem.append(motocicleta)
    print(f'\n✅ Motocicleta {modelo} cadastrada com sucesso!')
    

# Função de Consulta de motocicleta
def consulta(garagem):
    print('\n<< CONSULTA DE MOTOCICLETA >>')

    # verifica se há motocicletas cadastradas
    if garagem_vazia():
        return

    # recebe a moto para consultar
    moto_a_pesq = input('Digite a moto para pesquisar: ').strip()

    # verifica se foi digitado um nome válido
    if not moto_a_pesq:
        print('❌ Nome inválido!')
        return

    # inicial um loop pela lista garagem
    for moto in garagem:
        if moto_a_pesq.lower() == moto['modelo'].lower():
            print(f'\n✅ Motocicleta encontrada:')
            print('-' * 40)

            # print da motocicleta cadastrada
            for chave, valor in moto.items():
                print(f'  {chave.capitalize():15}: {valor}')
            print('-' * 40)
            return
    
    print(f'❌ A motocicleta {moto_a_pesq} não está cadastrada.')


# Função de atualizar quilometragem
def atualiza_quilometragem(garagem):
    print('\n<< ATUALIZAÇÃO DE QUILOMETRAGEM >>')

    # verifica se há motocicletas cadastradas
    if garagem_vazia():
        return

    # recebe o nome da moto para atualizar
    moto_a_atualizar = input('Digite a moto para atualizar: ').strip()

    # verifica se foi digitado nome válido
    if not moto_a_atualizar:
        print('❌ Nome inválido!')
        return

    # inicia um loop pela lista garagem
    for moto in garagem:
        if moto_a_atualizar.lower() == moto['modelo'].lower():
            print(f'Quilometragem atual: {moto["quilometragem"]} km')
            # se a moto estiver cadastrada solicita uma nova quilometragem
            try:
                km_atual = int(input('Digite a nova quilometragem: '))
            except ValueError:
                print('❌ Digite um número válido!')
                return

            # verifica se o km informado é igual ou menor que o que está cadastrado
            if km_atual < 0:
                print('❌ Quilometragem não pode ser negativa!')
                return
            elif km_atual == moto['quilometragem']:
                print('⚠️ A quilometragem é a mesma. Nenhuma alteração feita.')
                return
            elif km_atual < moto['quilometragem']:
                print('⚠️ A quilometragem digitada é menor que a cadastrada.')
                confirma = input('Deseja mesmo reduzir? (S/N): ').strip().lower()
                if confirma != 's':
                    return
            
            # atualiza a quilomentragem
            moto['quilometragem'] = km_atual
            print(f'✅ Quilometragem atualizada para {km_atual} km!')
            return
    
    print(f'❌ Motocicleta {moto_a_atualizar} não cadastrada!')

# Função de excluir motocicleta
def exclui(garagem):
    print('\n<< EXCLUSÃO DE MOTOCICLETA >>')

    # verifica se a lista garagem está vazia
    if garagem_vazia():
        return
    
    # recebe a motocicleta para excluir
    moto_a_excluir = input('Digite a moto para excluir: ').strip()
    if not moto_a_excluir:
        print('❌ Nome inválido!')
        return

    # inicia um loop pela lista garagem
    for i, moto in enumerate(garagem):
        if moto_a_excluir.lower() == moto['modelo'].lower():
            confirma = input(f'⚠️ Confirma exclusão de {moto_a_excluir}? (S/N): ').strip().lower()
            
            if confirma == 's' or confirma == 'sim':
                garagem.pop(i)  # ✅ Mais seguro que remove()
                print(f'✅ Motocicleta {moto_a_excluir} excluída com sucesso!')
            else:
                print(f'❌ Motocicleta {moto_a_excluir} NÃO foi excluída.')
            return
    
    print(f'❌ Motocicleta {moto_a_excluir} não está cadastrada.')



# Função de listar motocicleta
def listar(garagem):
    """Lista todas as motocicletas em formato de tabela"""
    print('\n<< LISTA DE MOTOCICLETAS >>')
    
    if garagem_vazia():
        return
    
    # ✅ Lista (não set!) para manter a ordem das colunas
    colunas = ['modelo', 'ano', 'cilindrada', 'cor', 'quilometragem']
    
    # Desenhar borda superior
    print('┌' + (19 * '─') * len(colunas) + '┐')
    
    # Cabeçalho
    print('│', end='')
    for coluna in colunas:
        print_palavra(coluna.capitalize())
    print()
    
    # Linha separadora
    print('├' + (19 * '─') * len(colunas) + '┤')
    
    # Dados
    for moto in garagem:
        print('│', end='')
        for chave in colunas:  # ✅ Agora usa a lista ordenada
            print_palavra(str(moto[chave]))
        print()
    
    # Borda inferior
    print('└' + (19 * '─') * len(colunas) + '┘')
    
    print(f'\n📊 Total: {len(garagem)} motocicleta(s)')


# Loop principal
def main():
    """Função principal do programa"""
    while True:
        opcao = menu()
        
        if opcao == 1:
            cadastro(garagem)
        elif opcao == 2:
            consulta(garagem)
        elif opcao == 3:
            atualiza_quilometragem(garagem)
        elif opcao == 4:
            exclui(garagem)
        elif opcao == 5:
            listar(garagem)
        elif opcao == 6:
            print('\n👋 Saindo do sistema... Até logo!')
            break
        
        input('\nPressione Enter para continuar...')


if __name__ == '__main__':
    main()