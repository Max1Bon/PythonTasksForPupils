import turtle
t = turtle.Pen()
t.pencolor("black")
t.width(4)
for n in range(4):
    t.circle(20)
    t.penup()
    t.forward(30)
    t.pendown()


