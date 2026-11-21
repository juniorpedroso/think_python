import turtle
import math

tela = turtle.Screen()
tela.setup(width=800, height=600)

t = turtle.Turtle()
tam_caneta = 3
t.pensize(tam_caneta)

# Dimensões do quadrado
lado = 100

# Posição inicial do quadrado
x = -390
y = 290

def rectangle(length, color):
    t.pendown()
    t.pencolor(color)
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.penup()

# Desenhando o quadrado
t.penup()
t.goto(x, y)
rectangle(lado, 'green')

# Calculando o centro do quadrado
centro_x = x + lado / 2
centro_y = y - lado / 2

# O raio máximo para caber dentro do quadrado é a metade do lado
raio = lado / 2

# Desenhando o polígono de 30 lados centralizado dentro do quadrado
n = 30
t.penup()

for i in range(n):
    angulo = i * (360.0 / n)
    rad = math.pi * angulo / 180
    px = centro_x + raio * math.cos(rad)
    py = centro_y + raio * math.sin(rad)
    
    if i == 0:
        t.goto(px, py)
        t.pendown()
        t.pencolor('blue')
    else:
        t.goto(px, py)

# Fecha o polígono voltando ao primeiro vértice
t.goto(centro_x + raio, centro_y)
t.penup()

turtle.done()