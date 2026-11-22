'''
Exercício 4 – Somando e calculando valores
Intermediário
Objetivo: praticar listas, laços for e acumulação.

Crie uma lista contendo os seguintes valores:
notas = [7.5, 8.0, 6.5, 9.0, 10.0]

1-Percorrer todos os elementos utilizando for.
2-Calcular a soma das notas.
3-Calcular a média.
4-Identificar a maior nota.
5-Identificar a menor nota.

Exemplo:
Soma das notas: 41.0
Média: 8.2
Maior nota: 10.0
Menor nota: 6.5
'''
notas = [7.5, 8.0, 6.5, 9.0, 10.0]

# inicialização das variáveis
maior_nota = notas[0]  # ✅ Inicializa com o primeiro valor
menor_nota = notas[0]  # ✅ Inicializa com o primeiro valor
soma = qtd_notas = media = 0

# iniciando o loop pelas notas
for nota in notas:

    # calculando a soma das notas
    soma += nota
    # calculando a quantidade de notas
    qtd_notas += 1
    # busca a nota maior
    if nota > maior_nota:
        maior_nota = nota
    # busca a nota menor
    if menor_nota != 0:
        if nota < menor_nota:
            menor_nota = nota
# calcula a médias das notas
media = soma / qtd_notas

print(f'Soma das notas: {soma}')
print(f'Média: {media}')
print(f'Maior nota: {maior_nota}')
print(f'Menor nota: {menor_nota}')
