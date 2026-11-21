# altura = int(input('Digite a altura da pirâmide: '))

# def triangle(altura):
#     for i in range(altura):
#         print('L' * (i + 1), end='')
#         print()

# triangle(altura)

"""
Write a function called rectangle that takes a string and two integers and draws a rectangle with the given width and height, 
made up using copies of the string. Here's an example of a rectangle with width 5 and height 4, made up of the string 'H'.

def rectangle(h, w, s):
    for i in range(h):
        print(s * w)

height = int(input('Digite a altura do quadrado: '))
width = int(input('Digite a largura do quadrado: '))
st = input('Digite a string: ')

rectangle(height, width, st)    
"""

"""
99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall


def first_line(n):
    print(f'{n} bottles of beer on the wall')

def second_line(n):
    print(f'{n} bootles of beer')
    print('Take one down, pass it around')

def last_line(n):
    print(f'{n-1} bootles of beer on the wall')
    print()


def bottle_verse(number):
    for i in range(number, 0, -1):
        first_line(i)
        second_line(i)
        last_line(i)
    
bottle_verse(2)
"""

def bottle_word(n):
    if n == 1:
        return 'bottle'
    else:
        return 'bottles'


def first_line(n):
    print(f'{n} {bottle_word(n)} of beer on the wall')


def second_line(n):
    print(f'{n} {bottle_word(n)} of beer')
    print('Take one down, pass it around')


def last_line(n):
    remaining = n - 1
    print(f'{remaining} {bottle_word(remaining)} of beer on the wall')
    print()


def bottle_verse(number):
    for i in range(number, 0, -1):
        first_line(i)
        second_line(i)
        last_line(i)


bottle_verse(2)