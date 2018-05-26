import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
# ask the user for the number of sides , default to 4 , min 2 , max 6

sides = int(turtle.numinput("Number of sides","How many sides in your spiral of spirals? (2-6)",4,2,6))

colors = ["red","yellow","blue","green","purple","orange"]

for m in range(100):
	t.forward(m*4)
	position = t.position()			#remember this corne
	heading = t.heading()			# remember this direction
	print(position,heading)
	# now inner spiral loop
	# draw a little spiral at each corner of the big spiral
	for n in range(int(m/2)):
		t.pendown()
		t.pencolor(colors[n%sides])
		t.forward(2*n)
		t.right(360/sides - 2)
		t.penup()
	t.setx(position[0])				# go back to the big spirals x location
	t.sety(position[1])
	t.setheading(heading)			
	t.left(360/sides + 2)
