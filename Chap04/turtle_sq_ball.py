import turtle

tela = turtle.Screen()
tela.setup(width=800, height=600)

t = turtle.Turtle()

# tamanho da caneta
tam_caneta = 3
t.pensize(tam_caneta)

# posiciona o quadrado no canto superior esquerdo
t.penup()
t.goto(-390, 290)

# desenhando um retangulo
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

# draw the circle
def polyline(n, length, angle):
    for i in range(n):
        t.pendown()
        t.forward(length)
        t.left(angle)
        t.penup()

def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)


rectangle(100, 'green')

# Position of circle
t.goto(-340,193)

polygon(n=30, length=9)

turtle.done()