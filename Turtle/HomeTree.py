import turtle

t = turtle.Turtle()

# Draw a brown house
t.color('brown')

# Draw base of house
for i in range(4):
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

# going to draw tree
t.right(30)
t.forward(50)
t.left(90)
t.color('white')        # setting color to white so that we cant see 
                        # we can either use penup() and pendown()

t.forward(150)

# drawing tree
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
