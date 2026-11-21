# constantes
number1 = 13
number2 = 17

def mdc(a, b):
    if b == 0:
        return a
    else:
        return (mdc(b, a % b))

print(mdc(number1, number2))
