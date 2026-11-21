texto = '''
Python é uma linguagem de programação.
Estou aprendendo Python!
Python é muito interessante.
'''

def word_in(word, target):
    if word in target:
        print(f'A palavra {word} existe no texto')
        quantidade = target.count(word)
        print(f'Ela aparece {quantidade} vezes')

    else:
        print(f'A palavra {word} não existe no texto')
    print('-+-' * 10)

word_in('Python', texto)

new_texto = texto.replace('Python', 'Java')

word_in('Java', new_texto)
word_in('Python', new_texto)
