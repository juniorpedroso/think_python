
print()
palavra = input('Digite a palavra: ')

def print_numbers():
    for s in range(7):
        for i in range(1,11):
            print(i % 10, end='')
    print()

def right_justify(palavra):
    print(f'Imprimindo {palavra} exatamente no final à direita')
    print_numbers()
    comprimento = len(palavra)
    n_space = 70 - comprimento - 1
    print(' ' * n_space, palavra)
    print()

def print_right(palavra):
    print(f'Imprimindo {palavra} de forma que a última letra fique na posição 40')
    print_numbers()
    comprimento = len(palavra)
    n_space = 40 - comprimento - 1
    print(' ' * n_space, palavra)
    print()

right_justify(palavra)
print_right(palavra)
    
