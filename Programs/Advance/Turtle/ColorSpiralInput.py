import turtle

t = turtle.Pen()
turtle.bgcolor("black")

#set up a list of any 8 valid python color names
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

#ask the user for number of sides beteween 1 and 8, with a default value 4

sides = int(turtle.numinput("Number of Sides","How many sides do you want (1-8)",4,1,8))

# draw a colorful spiral with the user specifide number of sides

for x in range(360):
	t.pencolor(colors[x%sides])		#only use the right number of colors
	t.forward(x * 3 / sides + x)		# change the size to match number of sides
	t.left(360 / sides + 1)			# turn 360 degrees / number of sides , plus 1
	t.width(x * sides / 200)		# Make the pen larger as it goes outward

