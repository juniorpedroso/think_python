import turtle

tela = turtle.Screen()
tela.setup(width=800, height=600)

t = turtle.Turtle()

# Posicione no canto esquerdo
t.penup()
t.goto(-390, 290)

# Começa a desenhar
t.pendown()

t.pencolor("red")
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

turtle.done()
