import turtle

t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.pencolor("bisque")
# first circle
t.fillcolor("bisque")
t.begin_fill()
t.circle(50)
t.end_fill()

# move pen to the other side
t.penup()
t.setpos(100, 0)
t.pendown()

# second circle
t.fillcolor("bisque")
t.begin_fill()
t.circle(50)
t.end_fill()

# first line of the shaft
t.left(90)
t.forward(250)

# head of the penis
t.fillcolor("brown")
t.begin_fill()
t.circle(50)
t.end_fill()

# rectangular shaft
t.fillcolor("bisque")
t.begin_fill()
t.left(90)
t.forward(100)

t.left(90)
t.forward(200)

t.left(90)
t.forward(100)
t.end_fill()

# creating the crack of the penis head
t.backward(45)
t.left(90)
t.forward(250)

# set pen color to green and write text
t.color("green")
t.write("Hello, World!", font=("Arial", 16, "normal"))

turtle.done()
