import turtle

t = turtle.Turtle()

# Draw a brown house
t.color('brown')

# Draw the base
for i in xrange(4):
    t.forward(50)
    t.left(90)

# Move up
t.penup()
t.left(90)
t.forward(50)
t.pendown()

# Draw the roof
t.right(30)
t.forward(50)
t.right(120)
t.forward(50)

t.right(30)
t.forward(50)
t.left(90)
t.color('white')

t.forward(150)
t.color('brown')

t.left(90)
t.forward(30)
t.color('green')
t.left(90)
t.forward(35)
t.right(130)
t.forward(45)
t.left(130)
t.forward(20)
t.right(130)
t.forward(50)

t.right(100)
t.forward(50)
t.right(130)
t.forward(20)
t.left(130)
t.forward(45)
t.right(130)
t.forward(35)
t.left(90)
t.color('brown')
t.forward(30)
