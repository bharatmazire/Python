import turtle
import time

colors = ['red' , 'purple' , 'blue' , 'green' , 'yellow' , 'orange']

t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)
	#time.sleep(0.000000)
