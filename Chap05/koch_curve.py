import turtle

def koch(t, x, n):
    """
    Desenha a curva de Koch.
    t: objeto turtle
    x: comprimento da linha
    n: profundidade da recursão (nível de detalhe)
    """
    if n == 0:
        t.forward(x)
    else:
        m = x / 3.0
        koch(t, m, n-1)
        t.left(60)
        koch(t, m, n-1)
        t.right(120)
        koch(t, m, n-1)
        t.left(60)
        koch(t, m, n-1)

# Exemplo de uso para desenhar um Floco de Neve (Koch Snowflake)
t = turtle.Turtle()
for _ in range(3):
    koch(t, 100, 3) # Tamanho 100, profundidade 3
    t.right(120)

turtle.done()