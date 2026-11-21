import turtle, math

""" 
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.done()

 """

# medida = 50
# turtle.pencolor('green')
# turtle.pensize(5)

# def change_color():
#     if turtle.pencolor() == 'green':
#         turtle.pencolor('red')
#     else:
#         turtle.pencolor('green')

# def square(n):
#     turtle.forward(n)
#     turtle.left(90)
#     turtle.forward(n)
#     turtle.left(90)
#     turtle.forward(n)
#     turtle.left(90)
#     turtle.forward(n)

# for i in range(16):
#     if i % 4 == 0:
#         medida += 50
#         change_color()
#     square(medida)

# turtle.done()

# import math

# def polygon(n, lenght):
#     angle = 360 / n
#     for i in range(n):
#         turtle.forward(lenght)
#         turtle.right(angle)

# def circle(radius):
#     circunference = 2 * math.pi * radius
#     n = 30
#     lenght = circunference / n
#     polygon(n, lenght)

# turtle.delay(10)
# circle(30)

def polyline(n, length, angle):
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)

def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

def circle(radius):
    arc(radius,  360)

turtle.delay(10)
polygon(n=20, length=9)
arc(radius=70, angle=70)
circle(radius=10)

turtle.done()