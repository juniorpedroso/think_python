# constantes
number1 = 12
number2 = 8

def gcd(a, b):
    lista_a = []
    lista_b = []

    # Criando a lista de divisores de number1
    for i in range(a):
        if a % (i + 1) == 0:
            lista_a.append(i + 1)

    # Criando a lista de divisores de number2
    for i in range(b):
        if b % (i + 1) == 0:
            lista_b.append(i + 1)

    # verificando as lista
    if len(lista_a) <= len(lista_b):
        for i in range(len(lista_a), 0, -1):
            if lista_a[i - 1] in lista_b:
                mdc = lista_a[i -1]
                return mdc
            
    else:
        for i in range(len(lista_b), 0, -1):
            if lista_b[i - 1] in lista_a:
                mdc = lista_b[i -1]
                return mdc

print(gcd(number1, number2))
