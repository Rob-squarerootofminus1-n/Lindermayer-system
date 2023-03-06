import turtle
from turtle import *
w = turtle.Screen()
w.bgcolor("thistle")

pen = turtle.Turtle()
angle = 30
pen.color('brown')
pen.speed = 1000000000
def arbre(n,lenght):
    if n==0:
        pen.color('green')
        pen.forward(lenght)
        pen.backward(lenght)
        pen.color('brown')
    else:
        width(n)
        pen.forward(lenght/3)
        pen.left(angle)
        arbre(n-1,lenght*2/3)
        pen.right(2*angle)
        arbre(n-1,lenght*2/3)
        pen.left(angle)
        pen.backward(lenght/3)
hideturtle()
pen.up()
pen.right(90)
pen.forward(300)
pen.left(180)
pen.down()
arbre(11,700)
showturtle()
mainloop()

turtle.exitonclick()
#try different angle values, it can be funny