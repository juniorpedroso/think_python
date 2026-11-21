
import turtle


# ==========================================
# CONFIGURAÇÕES
# t.speed(1)   # Muito lento
# t.speed(5)   # Velocidade intermediária
# t.speed(10)  # Muito rápido
# t.speed(0)   # Máxima velocidade
# ==========================================

X = -390
Y = 290

LADO = 400
COR = 'green'
MARGEM = 10
TAM_CANETA = 3
VELOCIDADE = 10

NUM_LADOS = 4


# ==========================================
# FUNÇÕES DE DESENHO
# ==========================================

def polygon(t, comprimento, num_lados, cor):
    """Desenha um polígono regular a partir da posição atual."""

    if num_lados < 3:
        raise ValueError('Um polígono precisa ter pelo menos 3 lados.')

    angulo = 360 / num_lados

    t.pencolor(cor)
    t.pendown()
    t.speed(VELOCIDADE)

    for _ in range(num_lados):
        t.forward(comprimento)
        t.right(angulo)

    t.penup()


def circle(t, centro_x, centro_y, raio, cor):
    """Desenha um círculo a partir de suas coordenadas centrais."""

    t.penup()
    t.speed(VELOCIDADE)
    t.goto(centro_x, centro_y - raio)
    t.setheading(0)

    t.pencolor(cor)
    t.pendown()
    t.circle(raio)
    t.penup()


def calcular_centro(x, y, lado):
    """Calcula o centro de um quadrado."""

    centro_x = x + lado / 2
    centro_y = y - lado / 2

    return centro_x, centro_y


# ==========================================
# INICIALIZAÇÃO DA TELA
# ==========================================

tela = turtle.Screen()
tela.setup(width=800, height=600)

t = turtle.Turtle()
t.pensize(TAM_CANETA)


# ==========================================
# DESENHO DO POLÍGONO
# ==========================================

t.penup()
t.goto(X, Y)

polygon(t, LADO, NUM_LADOS, COR)


# ==========================================
# DESENHO DO CÍRCULO
# ==========================================

centro_x, centro_y = calcular_centro(X, Y, LADO)

raio = (LADO - TAM_CANETA) / 2 - MARGEM

circle(t, centro_x, centro_y, raio, COR)


# ==========================================
# FINALIZAÇÃO
# ==========================================

turtle.done()
