import turtle

tela = turtle.Screen()
tela.setup(width=800, height=600)
tam_caneta = 3
cor_caneta = 'green'

t = turtle.Turtle()
t.pensize(tam_caneta)
t.pencolor(cor_caneta)


def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        t.forward(length)
        t.left(angle)
        draw(factor * length)
        t.right(2 * angle)
        draw(factor * length)
        t.left(angle)
        t.back(length)

draw(100)

turtle.done()