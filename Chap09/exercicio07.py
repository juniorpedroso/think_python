'''
Exercício 7 – Entendendo Aliasing e Copy
Intermediário / avançado
Objetivo: compreender a diferença entre referência e cópia de listas.

Execute o seguinte código:

lista_a = [10, 20, 30]      // [100, 20, 30]

lista_b = lista_a           // [100, 20, 30]

lista_c = lista_a.copy()    // [10, 200, 30]

lista_b[0] = 100

lista_c[1] = 200

print(lista_a)
print(lista_b)
print(lista_c)

Seu desafio:
1. Antes de executar, tente descobrir o resultado.
2. Execute o código no VS Code.
3. Explique por que lista_a e lista_b apresentam os mesmos valores.
4. Explique por que lista_c apresenta valores diferentes.
5. Utilize is e == para comparar as listas.

Pergunta adicional:

Qual será o resultado de:
print(lista_a is lista_b)       # False
print(lista_a is lista_c)       # False
print(lista_a == lista_c)       # False
'''

lista_a = [10, 20, 30]      # [100, 20, 30]

lista_b = lista_a           # [100, 20, 30]

lista_c = lista_a.copy()    # [10, 200, 30]

lista_b[0] = 100

lista_c[1] = 200

print(lista_a)
print(lista_b)
print(lista_c)

print(lista_a is lista_b)       # True
print(lista_a is lista_c)       # False
print(lista_a == lista_c)       # False
