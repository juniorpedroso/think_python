import re

'''
Utilize expressões regulares para:
1. Encontrar todos os números de telefone.
2. Mostrar os telefones encontrados.
3. Substituir todos os dígitos por *.
4. Mostrar o texto modificado.
Dica: utilize re.findall() e re.sub().
'''

texto = '''
Meu telefone é 11987654321.
O telefone de Maria é 21912345678.
O telefone de Pedro é 31987654321.
'''


# 1. Encontrar todos os números de telefone.
numeros = re.findall(r'\d+', texto)

# 2. Mostrar os telefones encontrados.
for numero in numeros:
    print(f'número encontrado: {numero}')
   
# 3. Substituir todos os dígitos por *.
novo_texto = re.sub(r'\d', '*', texto)

# 4. Mostrar o texto modificado.
print(novo_texto)