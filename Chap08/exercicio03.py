'''
01 Remover os espaços das extremidades.
02 Converter tudo para maiúsculas.
03 Converter tudo para minúsculas.
04 Substituir Python por programação.
05 Verificar se a frase começa com Aprendendo.
06 Contar quantas vezes aparece a letra a, sem diferenciar maiúsculas de minúsculas.
'''

import re

frase = '   Aprendendo Python é muito interessante   '

frase_clean = frase.strip()
frase_upper = frase_clean.upper()
frase_lower = frase_clean.lower()
frase_subst = frase_clean.replace('Python', 'programação')
frase_comeca = re.search('^Aprendendo', frase_clean)
frase_count = frase_lower.count('a')

print(frase_clean)
print(frase_upper)
print(frase_lower)
print(frase_subst)
if frase_comeca:
    print('A frase começa com Aprendendo')
else:
    print('A frase não começa com Aprendendo')
print(f'a aparece {frase_count} vezes')

