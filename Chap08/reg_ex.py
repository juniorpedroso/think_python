import re

texto = 'Estou aprendendo Java e Python.'

resultado = re.search('Python|Java', texto)
print(resultado.group())

resultado2 = re.findall('Python|Java', texto)
print(resultado2)

print('- ' * 30)
for i in resultado2:
    print(i)
print('- ' * 30)

texto = 'Meu telefone é (14)98801-8018.'

novo_texto = re.sub(r'\d', '#', texto)
print(novo_texto)

texto = 'Python é muito bom demais, é excelente'

print(re.search('^Python', texto))
print(re.search('excelente$', texto))