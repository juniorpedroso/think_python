import math

# constantes
coord_x1 = 0
coord_y1 = 0
coord_x2 = 3
coord_y2 = 4

def hypot(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    quadrado_dx = dx ** 2
    quadrado_dy = dy ** 2
    soma_quadrados = quadrado_dx + quadrado_dy
    solucao = math.sqrt(soma_quadrados)
    return solucao

print(hypot(coord_x1, coord_y1, coord_x2, coord_y2))
