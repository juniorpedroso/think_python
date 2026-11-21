import turtle, math


# posição inicial do elemento
x = -390
y = 290

# Características Gerais
comp_lado = 200
cor = 'green'
margem = 10

tam_caneta = 3
raio = ((comp_lado - tam_caneta) / 2) - margem



# função para desenhar polígono
def polygon(lenght, nLados, color):
    angle = 360 / nLados
    t.pendown()
    t.pencolor(color)
    for i in range(nLados):
        t.forward(lenght)
        t.right(angle)
    t.penup()

# função para desenhar um círculo
def circle(radius):
    circunference = 2 * math.pi * radius
    n = 30
    lenght = circunference / n
    polygon(lenght, n, cor)



num_lados =   4#int(input('Digite o num de lados: '))
# comprimento = 100 int(input('Digite o comprimento do lado: '))
cor_objeto =  'green' #input('Digite a cor do objeto: ')


# iniciando a tela
tela = turtle.Screen()
tela.setup(width=800, height=600)
t = turtle.Turtle()
t.pensize(tam_caneta)

# desenhando o polígono
t.penup()
t.goto(x,y)
polygon(comp_lado, num_lados, cor_objeto)

# desenhando um circulo para iniciar no meio do quadrado
len_circle = (2 * math.pi * raio) / 30
len_circle = len_circle / 2

new_x = x + int(((comp_lado / 2 - len_circle)))

new_y = y - margem
t.goto(new_x, new_y)
circle(raio)


turtle.done()
    