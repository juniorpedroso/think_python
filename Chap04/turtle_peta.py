import turtle, math

# Características iniciais
x = -400
y = 300
tam_caneta = 3
cor_caneta = 'green'

tela = turtle.Screen()
tela.setup(width=800, height=600)

t = turtle.Turtle()
t.pensize(tam_caneta)
t.pencolor(cor_caneta)
t.speed(0)


def polyline(n, length, angle):
    """Draws line segments with the given length and angle between them.
    
    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """ 
    for i in range(n):
        t.forward(length)
        t.right(angle)


def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)


# def arc(radius, angle):
#     arc_length = 2 * math.pi * radius * angle / 360
#     n = 30
#     length = arc_length / n
#     step_angle = angle / n
#     polyline(n, length, step_angle)

def arc(radius, angle, segments=60):
    """Desenha um arco."""
    arc_length = 2 * math.pi * radius * angle / 360

    length = arc_length / segments
    step_angle = angle / segments

    polyline(segments, length, step_angle)



# def petala(len, angle):
#     t.right(angle)
#     t.pendown()
#     arc(len,90)
#     t.left(270)
#     arc(len,90)
#     t.penup()

def petala(raio, angulo=60):
    """Desenha uma pétala."""
    for i in range(2):
        arc(raio, angulo)
        t.right(180 - angulo)


def flor(quantidade, raio):
    """Desenha uma flor com a quantidade de pétalas desejada."""

    if quantidade < 1:
        raise ValueError('A quantidade de pétalas deve ser positiva.')

    angulo = 360 / quantidade

    for i in range(quantidade):
        petala(raio)
        t.right(angulo)    


# Posicionamento inicial
t.penup()
t.goto(x + 150, y - 150)

# Desenhando a flor
t.pendown()
flor(6, 100)

t.penup()


turtle.done()
