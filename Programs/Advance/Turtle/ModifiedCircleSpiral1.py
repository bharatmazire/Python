import turtle

colors = ['red', 'blue', 'yellow', 'pink']
t = turtle.Pen()
turtle.bgcolor('black')

for x in range(100):
	t.color(colors[x%len(colors)])
	t.circle(x)
	t.left(91)
