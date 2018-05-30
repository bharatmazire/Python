import random
import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","gray"]
for n in range(50):
	# generate spirals of random sizes/colors at random locations on the screen
	t.pencolor(random.choice(colors))	# pick a random color from colors[]
	size = random.randint(10,40)		# pick a random spiral size from 10 to 40
	# generate a random (x,y) location on the screen
	x = random.randrange(0,turtle.window_width()//2)
	y = random.randrange(0,turtle.window_width()//2)

	# first spiral
	t.penup()
	t.setpos(x,y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(91)

	# second spiral
	t.penup()
	t.setpos(-x,y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(91)

	# third spiral
	t.penup()
	t.setpos(-x,-y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(91)

	# fourth spiral
	t.penup()
	t.setpos(x,-y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(91)
