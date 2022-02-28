import turtle

t = turtle.Turtle()

def cuadrado(lado, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(lado)
        t.right(90)
    t.end_fill()
    turtle.exitonclick()
        

def rect(base, altura, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(base)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()
    turtle.exitonclick()

def rombo(lado, color):
    t.fillcolor(color)
    t.begin_fill()
    t.right(45)
    cuadrado(lado)
    t.end_fill()
    turtle.exitonclick()

def hexa(lado, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(6):
        t.forward(lado)
        t.right(60)
    t.end_fill()
    turtle.exitonclick()

def trg(lado, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(lado)
        t.right(120)
    t.end_fill()
    turtle.exitonclick()

def para(base, altura, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(base)
        t.right(120)
        t.forward(altura)
        t.right(60)
    t.end_fill()
    turtle.exitonclick()

def circ(radio, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radio)
    t.end_fill()
    turtle.exitonclick()

#circ(50, '#00FF00')