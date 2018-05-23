import turtle

t = turtle.Pen()				# initialize pen
turtle.bgcolor("black")				# set background color to black
colors = ['red', 'yellow', 'blue', 'green']	# assign some colors in list

for x in range(100):				# loop 
	t.pencolor(colors[x%4])			# selecting color from list(colors = ['red', 'yellow', 'blue', 'green']) 
	t.circle(x)				# draw circle with color of radious x (value from 0 to 99)
	t.left(91)				# move pen head to 91 degree
