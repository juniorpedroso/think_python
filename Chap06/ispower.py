# A number,  a , is a power of  b  if it is divisible by  b  and  a/b  is a power of  b . 
# Write a function called is_power that takes parameters a and b and returns True if a is a power of b. 
# Note: you will have to think about the base case.

# constantes
number1 = 65536
number2 = 2

def is_power(a, b):
    if a % b == 0:
        #print(f'{a} é divisivel por {b}')
        divisao = a / b

        if divisao == 1:
            print(divisao)
            return True
        else:
            return is_power(divisao, b)
    else:
        print(f'{a} não é divisível por {b}')
        return False

print(is_power(number1, number2))
