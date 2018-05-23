import turtle


for i in range(2,7):
	t = turtle.Pen()
	turtle.bgcolor("black")
	sides = i
	colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
	for x in range(50):
		t.pencolor(colors[x%sides])
		t.forward(x * 3/sides + x)
		t.left(360/sides +1)
		t.width(x*sides/200)
	t.clear()
