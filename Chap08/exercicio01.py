import re
frase = 'Estou aprendendo Python.'

def analise_texto(texto):
    # funcoes
    comprimento = len(texto)
    # mostrar o primeiro caracter
    first_character = texto[0]
    # mostrar o último caracter
    last_character = texto[-1]
    # mostrar os últimos cinco caracteres
    last_five = texto[-5:]
    # mostrar a string invertida
    new_texto = ''
    for i in range(comprimento, 0, -1):
        old_letter = texto[i -1]
        new_texto = new_texto + old_letter
        
    # ✅ Forma Pythonica (1 linha)
    # texto_invertido = texto[::-1]
    
    # mostrar quantas vezes aparece a letra n
    n_times_n = texto.count('n')


    print(f'O comprimento do texto é {comprimento}')
    print(f'O primeiro carácter do texto é {first_character}')
    print(f'O último carácter do texto é {last_character}')
    print(f'Os últimos 5 carácteres do texto são {last_five}')
    print(f'O texto invertido fica assim: {new_texto}')
    print(f'A letra n aparece {n_times_n} vezes')



analise_texto(frase)
