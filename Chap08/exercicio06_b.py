import re

texto = '''
João tem 25 anos.
Maria tem 32 anos.
Pedro tem 18 anos.
Ana tem 45 anos.
'''

# Padrão de busca
padrao = r'\d+'

# 1. Localizar todos os números
numeros = re.findall(padrao, texto)

# 2. Mostrar cada número encontrado
for numero in numeros:
    print(numero)

# 3. Contar quantos números existem (usando len)
print(f'Qtd de números: {len(numeros)}')

# 4. Mostrar a soma das idades (usando sum + map)
total_idade = sum(map(int, numeros))
print(f'Total de idade = {total_idade}')
