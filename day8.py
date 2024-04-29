import turtle
import random
turtle.shape("turtle")
colors = ['red', 'blue', 'yellow', 'green', 'violet', 'orange']

for i in range(200):
    color = random.choice(colors)
    turtle.bgcolor('black')
    turtle.color(colors[i%6])
    turtle.speed(50)
    turtle.width(3)
    turtle.forward(10+5*i)
    turtle.right(89)
