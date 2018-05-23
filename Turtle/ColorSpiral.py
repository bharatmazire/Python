import turtle

t = turtle.Pen()							# initialize pen
turtle.bgcolor("black")							# setting background color to black

# you can choose between 2 and 6 sides for some cool shapes !

sides = 6								# setting sides

colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']		# listing some colors
for x in range(360):							# looping
	t.pencolor(colors[x%sides])					# selecting color from list
	t.forward(x * 3/sides + x)					# forwarding pen to some distance
	t.left(360/sides +1)						# moving pen head to some distance (here : 61)
	t.width(x*sides/200)						# setting pen width to some amount
