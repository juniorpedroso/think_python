
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
O telefone de Pedro é (31)98765-4321.
'''


# Padrão: 10 ou 11 dígitos isolados (telefone brasileiro)
# PADRAO_TELEFONE = r'\b\d{10,11}\b'
PADRAO_TELEFONE = r'\(?\d{2}\)?\s?9?\d{4}[-\s]?\d{4}'

# 1. Encontrar todos os números de telefone
telefones = re.findall(PADRAO_TELEFONE, texto)

# 2. Mostrar os telefones encontrados
print(f'{len(telefones)} telefones encontrados:')
for i, telefone in enumerate(telefones, start=1):
    print(f'  {i}. {telefone}')

# 3. Substituir todos os dígitos por *
texto_modificado = re.sub(r'\d', '*', texto)

# 4. Mostrar o texto modificado
print('\nTexto modificado:')
print(texto_modificado.strip())