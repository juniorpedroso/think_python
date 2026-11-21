x = 5
y = 7

# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')

# if x == y:
#     print(f'{x} é igual a {y}')
# elif x < y:
#     print(f'{x} é menor que {y}')
# else:
#     print(f'{x} é maior que {y}')


# def countdow_by_two(n):
#     if n <= 0:
#         print('Blastoff')
#     else:
#         print(n)
#         countdow_by_two(n -2)

# number = int(input('Digite um número: '))
# countdow_by_two(number)

# from time import time
# now = time()

# print(now)

# # constantes
# segundos_por_dia = 86400
# segundos_por_hora = 3600
# segundos_por_minuto = 60

# dias = now // segundos_por_dia
# print(f'Dias: {dias}')
# segundos_restantes = now % segundos_por_dia
# horas = segundos_restantes // segundos_por_hora
# print(f'Horas: {horas}')
# segundos_restantes = segundos_restantes % segundos_por_hora
# minutos = segundos_restantes // segundos_por_minuto
# print(f'Minutos: {minutos}')
# segundos_restantes = segundos_restantes % segundos_por_minuto
# print(f'Segundos: {segundos_restantes}')

from time import time

# Obtém o tempo atual em segundos desde a Unix epoch
now = time()

# Constantes de tempo
segundos_por_minuto = 60
segundos_por_hora = 3600  # 60 * 60
segundos_por_dia = 86400  # 24 * 3600

# Calcula o número de dias desde 1º de janeiro de 1970
dias = now // segundos_por_dia

# Calcula os segundos restantes no dia atual
segundos_restantes = now % segundos_por_dia

# Calcula horas, minutos e segundos do horário atual
horas = segundos_restantes // segundos_por_hora
minutos = (segundos_restantes % segundos_por_hora) // segundos_por_minuto
segundos = segundos_restantes % segundos_por_minuto

# Exibe os resultados
print(f'Dias desde a Unix epoch: {dias:.0f}')
print(f'Horário atual: {horas:.0f}:{minutos:.0f}:{segundos:.0f}')

# stick1 = int(input('Type lenght 0f stick 1: '))
# stick2 = int(input('Type lenght 0f stick 2: '))
# stick3 = int(input('Type lenght 0f stick 3: '))

# def is_triangle(l1, l2, l3):
#     triangle = True
#     if l1 > l2 and l1 > l3:
#         # bigger = l1
#         triangle = (l1 < (l2 + l3))

#     elif l2 > l1 and l2 > l3:
#         # bigger = l2
#         triangle = (l2 < (l1 + l3))
#     else:
#         # bigger = l3
#         triangle = (l3 < (l1 + l2))

#     return triangle

# if is_triangle(stick1, stick2, stick3):
#     print('É possível formar um triangulo com estas três varetas.')
# else:    
#     print('Não é possível formar um triangulo com estas três varetas.')


# from time import time

# # Obtém o tempo atual em segundos desde a Unix epoch
# now = time()

# # Constantes de tempo
# segundos_por_minuto = 60
# segundos_por_hora = 3600  # 60 * 60
# segundos_por_dia = 86400  # 24 * 3600

# dias = now // segundos_por_dia
# segundos_restantes = now % segundos_por_dia
# horas = segundos_restantes // segundos_por_hora
# minutos = (segundos_restantes % segundos_por_hora) // segundos_por_minuto
# segundos = (segundos_restantes % segundos_por_hora) % segundos_por_minuto

# print(f'dias: {dias}')
# print(f'horas: {horas}')
# print(f'minutos: {minutos}')
# print(f'segundos: {segundos}')

