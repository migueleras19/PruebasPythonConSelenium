import turtle
from random import randint

def get_input_angle():
    message = 'Ingrese el angulo por favor: '
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        
        print('la entrada debe ser un número entero!')
        value_as_string = input(message)
        
    return int(value_as_string)

def generar_color_aletorio():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

print('Configurar Pantalla')

turtle.title('Patron de color')
turtle.setup(740, 700)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(10)
angle = get_input_angle()

print('Dibujando...')

for i in range(0, 200):
    turtle.color(generar_color_aletorio())
    turtle.forward(i)
    turtle.right(angle)
    
print('Realizado..')

turtle.done()