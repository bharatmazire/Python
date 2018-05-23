# importing required library
import turtle
import time

# initializing pen
t1 = turtle.Pen()
t2 = turtle.Pen()

# setting background color
turtle.bgcolor('black')

# setting pen color
t1.pencolor('red')
t2.pencolor('red')

# setting pen width
t1.width(1)
t2.width(1)

# rotating cursors
t1.left(90)
t2.left(90)

# loop for drawing curves
for i in range(230):
	t1.forward(1)
	t1.left(1)
	t2.forward(1)
	t2.right(1)

# loops for drawing stright line
for i in range(135):
	t1.forward(1)
	t2.forward(1)
	
# sleep to see changes
time.sleep(3)
