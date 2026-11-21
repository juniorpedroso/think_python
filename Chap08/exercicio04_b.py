def is_palindrome(palavra):
    # 1. Converte para minúsculas
    # 2. Remove TODOS os espaços (não só das pontas)
    palavra_limpa = palavra.lower().replace(" ", "")
    
    # 3. Compara a string com ela mesma invertida
    # [::-1] é um atalho do Python para inverter sequências
    return palavra_limpa == palavra_limpa[::-1]

# Testes
print(is_palindrome("arara"))          # True
print(is_palindrome("   Arara   "))    # True (ignora espaços e maiúsculas)
print(is_palindrome("a mala nada na lama")) # True (funciona com frases!)
print(is_palindrome("python"))         # False