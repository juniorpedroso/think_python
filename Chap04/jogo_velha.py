import turtle

tela = turtle.Screen()
tela.setup(width=800, height=600)

t = turtle.Turtle()

# tamanho da caneta
tam_caneta = 3
t.pensize(tam_caneta)

# Posicione no canto esquerdo
t.penup()
t.goto(-390, 290)




def rectangle(lenght, color):
    # Começa a desenhar
    t.pendown()
    t.pencolor(color)
    t.forward(lenght)
    t.right(90)
    t.forward(lenght)
    t.right(90)
    t.forward(lenght)
    t.right(90)
    t.forward(lenght)
    t.right(90)
    t.penup()

def next_coord(new_x, new_y):
    atual_xcor = t.xcor()
    print(atual_xcor)
    atual_ycor = t.ycor()
    print(atual_ycor)
    t.goto(atual_xcor + new_x, atual_ycor+ new_y)


       

rectangle(100, 'black')

next_coord(106, 0)
rectangle(100, 'black')

next_coord(106, 0)
rectangle(100, 'black')

# second line

next_coord(-212, -106)
rectangle(100, 'black')

next_coord(106, 0)
rectangle(100, 'black')

next_coord(106, 0)
rectangle(100, 'black')

# third line

next_coord(-212, -106)
rectangle(100, 'black')

next_coord(106, 0)
rectangle(100, 'black')

next_coord(106, 0)
rectangle(100, 'black')






turtle.done()