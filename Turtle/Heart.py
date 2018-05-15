import turtle
import time

t1 = turtle.Pen()
t2 = turtle.Pen()
turtle.bgcolor('black')
t1.pencolor('red')
t2.pencolor('red')
t1.width(1)
t2.width(1)
t1.left(90)
t2.left(90)
for i in range(230):
	t1.forward(1)
	t1.left(1)
	t2.forward(1)
	t2.right(1)
for i in range(135):
	t1.forward(1)
	t2.forward(1)
time.sleep(3)
